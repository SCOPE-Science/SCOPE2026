"""Reproducible checks for the full central-section side law of triangular prisms."""
import math
import numpy as np


def exact(h):
    assert h > 0
    p3 = 6 / math.pi * math.atan(h*h/(math.sqrt(3)*(4+h*h+4*math.sqrt(1+h*h/3))))
    mean = 6/math.pi*math.acos((h*h-2)/(h*h+4)) + 3/math.pi*math.acos((4-h*h)/(4+h*h))
    return {3:p3, 4:5-mean-2*p3, 5:mean-4+p3},mean


def empirical(h, rng, n=180000):
    u = np.array([[math.cos(2*math.pi*j/3),math.sin(2*math.pi*j/3)] for j in range(3)])
    vert = np.array([np.r_[u[j],z*h/2] for z in (-1,1) for j in range(3)])
    edges = [(j, (j+1)%3) for j in range(3)]
    edges += [(j+3, (j+1)%3+3) for j in range(3)]
    edges += [(j, j+3) for j in range(3)]
    normals=rng.normal(size=(n,3));normals/=np.linalg.norm(normals,axis=1)[:,None]
    dots=normals@vert.T
    count=np.zeros(n,dtype=np.int16)
    for i,j in edges:
        count+=(dots[:,i]*dots[:,j] < 0)
    assert np.all(np.isin(count,[3,4,5]))
    return {i:np.mean(count==i) for i in (3,4,5)}, np.mean(count)


def main():
    rng=np.random.default_rng(1729)
    for h in (.25,1.0,2.0,5.0,10.0):
        prob,expected=exact(h)
        assert all(0 <= x <= 1 for x in prob.values()),(h,prob)
        assert abs(sum(prob.values())-1)<1e-12
        assert abs(sum(i*prob[i] for i in (3,4,5))-expected)<1e-12
        sample,observed=empirical(h,rng)
        assert all(abs(prob[i]-sample[i])<0.008 for i in (3,4,5)),(h,prob,sample)
        assert abs(observed-expected)<0.016
        print(h,prob,sample)
    print('PASS: five heights, all 9 edge signs, probabilities and means.')


if __name__=='__main__':main()
