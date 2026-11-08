# Independent mathematical audit

## correctness

PASS

Use zero-hub W0=span{x,x²} with Gram inverse [[48,-60],[-60,80]], orthogonal complement hub function q=1-4x+(10/3)x² of squared L2 norm 1/9. Kernel K_ij=delta_ij K0+9q(x)q(y)/k, so tip evaluation has quadratic p_t(y)=10(2+t)y²-12(1+t)y+3t on its edge and 3t q on other edges, t=1/k. Integrate absolute values via two interior roots and discriminant 24(t²+2t+6); derivative of h(t)=(t²+2t+6)^(3/2)/(t+2)² has sign t-1. Reproduction of constant 1 makes negative-kernel mass (E_k-1)/2. Fresh independent exact Gram inversion verified for stars k1..4 at all sampled edges, and inspected source SymPy script of 18 further k. Distinguish point-evaluation norm from global operator norm.

## originality

PASS

General de Boor/Shadrin spline-projector norm boundedness does not determine this exact value at leaves, nor branch monotonicity and positivity threshold. Kayumov works with second-order differential-operator L-splines, and Arioli–Benzi with linear quantum-graph finite elements. Published affine-simplex projector positivity concerns a different polynomial space and domain. Best-of-knowledge original exact star-quadratic norm is not automatic from qualitative boundedness, though elementary Gram specializations could have been previously tabulated.

## value

PASS

The natural sensitivity of least-squares projection at leaves and exact loss of positivity matter for stability of polynomial reconstruction on branching networks; one formula classifies every branching count and reveals a nontrivial sharp threshold. It is not presented as the full global norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
