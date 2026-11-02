# Independent mathematical audit

## correctness

PASS

PASS. Differentiate ((1-y²)w_{p,q})'=(p-q-(p+q)y)w_{p,q} on (-1,1) and integrate against e^{ity}; endpoint flux vanishes for every p,q>0 even if the original density diverges integrably. The resulting ODE is tH''+(p+q)H'+tH=i(p-q)H, H(0)=1, H'(0)=i(p-q)/(p+q). Multiplication by conjugate and subtraction yields (t^m W)'=2i(p-q)t^{m-1}|H|² with no integration constant at zero; therefore Im(H' conjugate H)=(p-q)t^{-m} integral_0^t s^{m-1}|H(s)|² ds for all t>0. This is strictly signed because H(0)=1; any nonzero real H zero would force the Wronskian to vanish, impossible. Reflection symmetry extends sign to negative frequencies; the unwrapped phase exists and derivative has the sign of p-q. On the diagonal the Fourier-Bessel identity gives simple zeros +/-j_{nu,k}. At fixed m, implicit differentiation of the ODE in delta=p-q and the mixed Wronskian at a simple Bessel zero gives t_k'(0)=i integral_0^j J_nu(s)^2 ds / (j J_nu'(j)^2)>0. Fixed-order Bessel large-j asymptotics give numerator (1/pi)log j+O(1) and denominator 2/pi+O(1/j), hence the logarithmic velocity. Independently evaluated the Wronskian at asymmetric shape triples with numerical residual ~10^-40 and located complex zeros for delta=+/-0.0001; observed velocity agrees with the Bessel integral. These are diagnostics, not an infinite proof; the source ODE/implicit-function argument establishes all quantifiers, including parameter-shape endpoints.

## originality

PASS

PASS, substantially qualified: the real-zero dichotomy for beta shapes >=1 is explicitly mentioned in a 2005 beta-wavelet primary paper and MUST NOT be claimed new on that range. The independently derived global phase Wronskian/strict phase law, extension to all p,q>0, and exact complex-zero velocity including k-growth form the remaining distinct claim.

## value

PASS

PASS. The exact integral phase derivative and the first-order imaginary escape speeds are natural global analytic invariants for an entire family of Fourier transforms. They give a quantitative strengthening beyond known qualitative wavelet spectral notches and the classical Bessel diagonal, including a nontrivial logarithmic growth law. The result is substantive even after explicitly excluding the older real-zero observation from novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
