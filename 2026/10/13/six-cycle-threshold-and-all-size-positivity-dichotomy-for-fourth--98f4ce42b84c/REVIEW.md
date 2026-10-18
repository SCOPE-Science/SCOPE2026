# Independent mathematical audit

## correctness

PASS

For n≥3, Q_n=-L(C_n) with two unit-rate neighbors and R(z)=(12+6z+z²)/(12-6z+z²), an independently reconstructed matrix polynomial identity gives all circulant distance coefficients at n=3,4,5,6; numerators strictly >0 for h>0 at n<=5. At n6, denominator D6=(h²+6h+12)(3h²+6h+4)(4h²+6h+3)>0, all entries except adjacent are positive, and adjacent = -2h F6(h)/D6 for F6=5h^4-12h^3-102h²-144h-72. Descartes one sign change and F6(6)<0<F6(7) give unique positive h6≈6.36885080963; h7 adjacent=-25354/4790839. For general fixed n≥6, R(-hλ)=1-12/(hλ)+O(h^-2), T_n=I-12L_n^+/h+O_n(h^-2), and (L_n^+)_{0,1}=(n-1)(n-5)/(12n)>0. Thus adjacent entries eventually negative with coefficient -(n-1)(n-5)/(n h). Spectrum R(-t) in (0,1) for t>0 establishes SPD contraction and unit row sums throughout. Independent polynomial certificates and exact rational pseudoinverse tests corroborate; all-n proof analytical.

## originality

PASS

The inspected original Padé-positive-systems papers establish general loss of positivity and examples, not the exact uniform-cycle n=5/6 boundary and six-cycle quartic. Resultary prior eight-state Padé Markov barrier is for a pure-birth chain with arbitrarily-small-step negativity, not symmetric periodic nearest-neighbor large-step loss; another lattice result uses filtered Crank--Nicolson, not this [2/2] Padé propagator. Universal absolute-monotonicity facts cannot imply this special system classification without additional structural analysis.

## value

PASS

Periodic diffusion chains are canonical Markov models; the theorem gives a sharp size boundary and exact first-failure step window for standard fourth-order A-stable Gauss--Legendre time stepping, demonstrating where spectral stability and conservation fail to guarantee nonnegative transition probabilities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
