# Independent mathematical audit

## correctness

PASS

For all integer n>=2 and q>=1, convolution differentiation and a sign input attain exactly the normalized total variation of the powered Fejer kernel. Strict logarithmic concavity in each complete noncentral nodal lobe yields a unique stationary maximum satisfying n*cot(nu)=cot(u), with explicit peak M_{n,k}; central/side and odd-terminal variations give the exact finite numerator. Parseval gives Z=n^{-q} sum_j c_j^2. For fixed q, t=2u/n rescaling gives the sinc^{2q} integral, stationary roots tan r=r and summable k^{-2q} lobe envelope. For high q, write H_n=F_n/n and expand log H_n(t)=-(n^2-1)t^2/12+O(n^4 t^4) uniformly near zero, yielding a uniform Laplace mass sqrt(12*pi/[q(n^2-1)]). A uniform <1 gap off the center plus the tail envelope makes all other lobes O(4^{-q}) in total variation; the resulting norm is sqrt(q(n^2-1)/(3*pi)) uniformly n>=2. Boundary cases n=2, odd n and q=1 included; real and complex L∞ sign attainment are both valid. The independent numerical tests are supporting checks only; no finite test establishes a quantified limit.

## originality

PASS

Best-of-knowledge originality for the three-part exact sharp rough-input Fejer-power norm result: the family of generalized Jackson kernels is explicitly known (Runovski–Schmeisser §5), and sign-duality itself is elementary; inspected primary papers instead prove Fejer approximation/periodization, polynomial convergence and Lp convergence, without a formula for the total-variation norm, the sinc-sidelobe root series or uniform high-power/frequency Gaussian limit. Published related exact-norm records concern different operators. Inaccessible Greiner 1999 full text is named, not declared noncovering; an equivalent sharp-variation result remains possible.

## value

PASS

Sharp rough-input L∞→Lipschitz amplification is a natural quantitative stability invariant of positive smoothing on the circle, distinct from ordinary Fejer approximation rates. The finite all-(n,q) extrema formula, fixed-power sinc side-lobe limiting constants, and rigorously uniform two-parameter high-power Gaussian law provide a reusable complete classification of this family, not an arbitrary small-slice computation. The same kernels were previously studied for Lp convergence, making the extra sharp endpoint result mathematically motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
