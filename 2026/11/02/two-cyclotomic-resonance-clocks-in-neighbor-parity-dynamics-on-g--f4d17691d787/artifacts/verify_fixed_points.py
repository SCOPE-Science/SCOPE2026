"""Independent fixed-state exponent check for generalized Petersen parity dynamics."""
from verify_fixed import nullity_poly

def verify():
    count=0
    for n in range(5,401):
        e=n&-n
        expected=min(2,e)+4*(n%5==0)
        found=nullity_poly(n,1)
        assert found==expected,(n,found,expected)
        count+=1
    print('OK exact fixed-point exponent tests',count)
if __name__=='__main__':verify()
