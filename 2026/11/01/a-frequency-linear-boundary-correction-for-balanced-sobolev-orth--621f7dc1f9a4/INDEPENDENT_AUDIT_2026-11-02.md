# Independent mathematical audit

## correctness

PASS

For fixed integer m>=1, |a|<1/2 and lambda>0, the monomial Gram matrix for the n^-2 derivative weight is Hermitian, diagonal 1+lambda j²/n², and off-diagonals only at |j-k|=m with magnitude |a|lambda jk/n². Residues mod m split, and the monic Schur pivot satisfies h_j=1+lambda(j/n)^2-|a|²lambda²j²(j-m)²/(n^4 h_(j-m)). Positive lower bound D(j/n)/2 follows from |a|<1/2; the step-map derivative is uniformly rho<1 for n large. Stable fixed point H=(D+sqrt(D²-4|a|²lambda² x^4))/2 and correction E_m(x)=2m|a|²lambda² x³/Delta(x)² satisfy the pivot recursion with O(n^-2) residual, propagated globally by contraction from small j. At x=1 obtain sigma_n²=(1+lambda+Delta)/2+2m|a|²lambda²/(n Delta²)+O(n^-2), Delta²=(1+lambda)²-4|a|²lambda². For a=0 exact sigma_n²=1+lambda. Independently compared full exact rational Gram minimizations against pivots in 176 cases and checked n²-scaled residuals for m=1,3,7 at n=200,400,800,1600; these are corroborations, not asymptotic proof.

## originality

PASS

PASS best-of-knowledge. The closest and now fully accessible primary 2026 Majumder–Swaminathan article was inspected: its critical Sobolev squared norms receive only Proposition 1 leading upper/lower bounds; Theorem3.2 gives outer polynomial asymptotics, not this explicit harmonic-m linear 1/n norm coefficient. Other results supply background but no demonstrated implication; residual general recurrence priority risk stated.

## value

PASS

The n^-2 derivative coupling is the natural critical scaling for degree-n circle polynomials. The leading norm loses all Fourier harmonic index information, but the exact first correction recovers frequency m linearly. A controlled all-m first-order boundary term with O(n^-2) remainder is a motivated new structural quantitative asymptotic rather than routine leading-order restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
