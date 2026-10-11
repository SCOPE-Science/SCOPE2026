# Independent mathematical audit

## correctness

PASS

Radial inversion with the stated Fourier normalization gives \(K_\delta(r)=(2\pi\delta r)^{-1}\int_{1-\delta/2}^{1+\delta/2}\rho J_1(r\rho)\,d\rho\). On \(1\le r\le\varepsilon/\delta\), the transition average differs from the disc kernel \(K_0(r)=J_1(r)/(2\pi r)\) by \(O(\varepsilon r^{-3/2})\). Beyond that scale, one integration by parts in the oscillatory average gives \(O(\delta^{-1}r^{-5/2})\), whose \(L^{4/3}\) tail contributes only \(O_\varepsilon(1)\). The replacement error on the logarithmic core is \(O(\varepsilon\log(1/\delta))+O_\varepsilon(1)\). Finally \(J_1(r)=\sqrt{2/(\pi r)}\cos(r-3\pi/4)+O(r^{-3/2})\), so the radial integral reduces to the periodic mean of \(|\cos|^{4/3}\). Independently recomputing the constants gives \(2\pi(2^{-2/3}\pi^{-2})\cdot \pi^{-1}\mathrm B(1/2,7/6)=2^{1/3}\pi^{-2}\mathrm B(1/2,7/6)\), exactly as claimed.

## originality

PASS

Carbery and Seeger's primary paper uses exactly the same trapezoidal multiplier and Fourier convention. It states that the endpoint kernel norm is comparable to \((\log(1/\delta))^{3/4}\) and explicitly defines its symbol 'approximately' as two-sided comparability; the paper's main exact-sharp result concerns the larger multiplier norm. A full-document search of the primary PDF for the kernel, asymptotic language, Beta functions and Bessel references found no stated leading coefficient for the kernel norm. The audited theorem requires isolating the transition scale and averaging the oscillatory Bessel leading term to obtain a limit rather than comparability. Current Resultary search returned the assigned coefficient as the exact same-object hit and no stronger prior formula.

## value

PASS

The primary paper itself singles out the endpoint kernel scale because it separates from the operator-norm scale. Determining the actual normalized limit for its canonical rough mollifier converts an order statement into a sharp benchmark and identifies the oscillatory angular-average constant. The exact coefficient is narrow but naturally motivated by the sharp endpoint analysis and is not a recomputation of a known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
