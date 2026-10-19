"""Finite exact checks for logarithmic ballistic-front aging in persistent walks."""
import numpy as np

def run():
    for c in (0.6, 1.0, 1.5):
        n=300000
        m=1200
        rng=np.random.default_rng(6301+int(c*100))
        flips=np.zeros((m,),dtype=np.int32)
        second=np.zeros((m,),dtype=np.int32)
        spin=np.where(rng.random(m)<0.5, -1, 1).astype(np.int8)
        x=np.zeros(m,dtype=np.int32)
        log_surv=np.zeros(n+1)
        for k in range(1,n+1):
            p= c/(k*np.log(k)) if k>=4 else 0.0
            if p>=1: raise ValueError('invalid rate')
            did = rng.random(m) < p
            second[did]=flips[did]
            flips[did]=k
            spin[did] *= -1
            x += spin
            log_surv[k]=np.log1p(-p)
        # Use the finite-N product for the last-flip CDF, not a limiting approximation.
        suffix=np.cumsum(log_surv[::-1])[::-1]
        observed=[]
        expected=[]
        for u in (0.35,0.5,0.65,0.8):
            cutoff=int(n**u)
            empirical=np.mean(flips<=cutoff)
            exact=np.exp(suffix[cutoff+1])
            assert abs(empirical-exact)<0.06,(c,u,empirical,exact)
            observed.append(float(empirical));expected.append(float(exact))
        loss=n-np.abs(x)
        bound=(flips<n//2)&(flips>0)
        # With a last flip before the middle, the current sign determines the actual front.
        assert np.all((loss[bound]>=2*(flips[bound]-np.maximum(second[bound],1))) & (loss[bound]<=2*flips[bound]))
        print('c',c,'finite_CDF',observed,'exact_CDF',expected,
              'last_flip_front_bounds_checked',int(bound.sum()))
    print('All finite product and pathwise front bounds passed.')

if __name__=='__main__':run()
