# A sharp symmetry-breaking threshold for two-compartment Haldane–Andrews allocation

## Finding

Let \(b\geq 0\), \(N>0\), and let
\[
f_b(s)=\frac{s}{1+bs+s^2},\qquad I_{N,b}(x)=f_b(x)+f_b(N-x),\qquad 0\leq x\leq N.
\]
There is a unique \(L_b\geq 2\sqrt3\) satisfying
\[
L_b^3-12L_b-8b=0.
\]
The following is the complete global and local optimum classification for every such \(b,N\):

1. If \(0<N<L_b\), the unique global maximizer is the equal allocation \(x=N/2\); it is the only interior stationary point and is a strict local maximum. Both endpoints are strict one-sided local minima.
2. At \(N=L_b\), the equal allocation remains the unique strict global maximum, but its quadratic curvature vanishes. Its first nonconstant local Taylor term is negative and quartic. Both endpoints remain strict one-sided local minima.
3. If \(N>L_b\), equal allocation becomes a strict local minimum. Exactly two additional interior stationary points exist, both strict global and local maxima, at
\[
x_{\pm}=\frac{N\pm\sqrt{N^2-4u_*}}{2},\qquad
u_* = \frac{(N+b)\sqrt{N^2+2bN+4}-N}{N+2b}.
\]
There are no other stationary points or global maximizers, and the endpoints remain strict one-sided local minima.

The asymmetric optima emerge continuously with a sharp square-root onset:
\[
\left|\frac{x_{\pm}}{N}-\frac12\right|
=\sqrt{\frac{3(L_b^2-4)}{8L_b^2}}\,
\sqrt{\frac{N}{L_b}-1}
+o\!\left(\sqrt{\frac{N}{L_b}-1}\right)
\quad(N\downarrow L_b).
\]
For fixed \(b\geq0\), the smaller optimal allocation tends to the unique single-compartment growth-rate maximizer \(s=1\):
\[
\min(x_+,x_-)=1+\frac{(b+2)^2}{2N^2}+O_b(N^{-3}),
\qquad
\max_x I_{N,b}(x)=\frac1{b+2}+\frac1N+O_b(N^{-2}).
\]
In contrast, the equal-allocation performance is \(I_{N,b}(N/2)\sim 4/N\) and tends to zero.

## Assumptions and scope

This is an instantaneous, fixed-biomass optimization of a **prescribed total substrate concentration** across two identical, equal-volume, noninteracting compartments. The kinetic law is the substrate-inhibited Haldane–Andrews specific-growth function, not a population-dynamic equation. With conventional dimensional concentrations \(S_i\) and positive kinetic parameters \(K_s,K_i,\mu_{\max}\),
\[
\mu(S)=\frac{\mu_{\max}S}{K_s+S+S^2/K_i},\qquad
s_0=\sqrt{K_sK_i},\quad b=\sqrt{K_i/K_s},\quad x=S_1/s_0,\quad N=(S_1+S_2)/s_0.
\]
Then \(\mu(S_1)+\mu(S_2)=\mu_{\max}(s_0/K_s)I_{N,b}(x)\). All physical \(K_s,K_i\) give \(b>0\); the boundary \(b=0\) is an included mathematical limit. Equal fixed biomass makes maximization of the sum of specific growth rates proportional to instantaneous aggregate biomass production. No variable populations, residence times, nutrient mass transport, unequal volumes, or long-time reactor behavior are asserted.

## Proof

**Reduction to the product coordinate.** For \(u=x(N-x)\), the full allocation interval maps onto \(0\leq u\leq N^2/4\), with each interior \(u<N^2/4\) represented by the two reflected allocations. Combining rational denominators gives the exact identity
\[
I_{N,b}(x)=J_{N,b}(u)
=\frac{N+(N+2b)u}{H_{N,b}(u)},
\qquad
H_{N,b}(u)=u^2+(b^2+bN-2)u+N^2+bN+1.
\]
The denominator equals
\((1+bx+x^2)(1+b(N-x)+(N-x)^2)>0\).
The sign of its derivative is therefore the sign of the quadratic polynomial
\[
H_{N,b}(u)^2 J'_{N,b}(u)=G_{N,b}(u)
=N^3+2bN^2+b^2N+3N+2b-2Nu-(N+2b)u^2.
\]
For every \(u\geq0\),
\[
G_{N,b}(0)>0,\qquad G'_{N,b}(u)=-2N-2(N+2b)u<0.
\]
At the endpoint of the feasible product interval, direct factorization yields
\[
G_{N,b}(N^2/4)=
\frac{(N^2+2bN+4)(12N+8b-N^3)}{16}.
\]
The cubic \(N^3-12N-8b\) has exactly one positive zero: it is negative at \(N=2\sqrt3\), and its derivative is positive thereafter. That zero is \(L_b\), with equality \(L_0=2\sqrt3\).

For \(N<L_b\), \(G\) is strictly positive throughout \([0,N^2/4]\), so \(J\) increases strictly to its right endpoint; only equal allocation maximizes. For \(N>L_b\), the strictly decreasing \(G\) crosses zero exactly once in \((0,N^2/4)\); its positive zero is
\[
u_* = \frac{-N+\sqrt{N^2+(N+2b)(N^3+2bN^2+b^2N+3N+2b)}}{N+2b}
=\frac{(N+b)\sqrt{N^2+2bN+4}-N}{N+2b}.
\]
Thus \(J\) strictly increases to \(u_*\) and strictly decreases afterwards, proving both the formula and global optimality. On \(0<x<N/2\), the product coordinate increases strictly, and on \(N/2<x<N\) it decreases strictly; the resulting stationary-point types follow. As \(G(0)>0\), moving inward from either allocation endpoint strictly improves the objective, proving the one-sided minimum statements.

At \(N=L_b\), \(G\) remains positive for all \(u<N^2/4\), while \(G(N^2/4)=0\). Since \(G'(N^2/4)<0\), one has \(J''(N^2/4)<0\). The identity \(u=N^2/4-(x-N/2)^2\) then yields
\[
I_{N,b}(N/2+h)-I_{N,b}(N/2)
=\tfrac12J''_{N,b}(N^2/4)h^4+O(h^6),
\]
which is strictly negative for small nonzero \(h\), proving the quartic critical maximum.

**Onset.** Let \(d(N)=N^2-4u_*(N)\). The explicit root formula or implicit differentiation of \(G_{N,b}(u_*)=0\) at \(N=L_b\), \(u_*=L_b^2/4\), gives
\[
d(L_b)=0,\qquad d'(L_b)=\frac{3(L_b^2-4)}{2L_b}>0.
\]
As \(|x_\pm/N-1/2|=\sqrt{d(N)}/(2N)\), Taylor's theorem gives the stated square-root coefficient.

**Large budgets.** For fixed \(b\geq0\), expansion of the displayed positive root yields
\[
u_*(N)=N-1+\frac{(b+2)^2}{2N}+O_b(N^{-2}).
\]
The smaller root of \(x(N-x)=u_*\) is \(x_{\min}=2u_*/(N+\sqrt{N^2-4u_*})\), so
\[
x_{\min}=1+\frac{(b+2)^2}{2N^2}+O_b(N^{-3}).
\]
Because \(f_b'(1)=0\), the small compartment contributes \(1/(b+2)+O_b(N^{-4})\), while the large one contributes \(1/N+O_b(N^{-2})\). The equal split has \(I_{N,b}(N/2)=N/(1+bN/2+N^2/4)\sim4/N\), completing the asymptotic comparison.

**Exact example.** For \(b=2\), the positive root of the threshold cubic is \(L_2=4\). At \(N=6\), the optimizing product is \(u_*=29/5\), with the two allocations \(x_\pm=3\pm4/\sqrt5\). The maximum value is \(25/64\), whereas equal allocation yields \(3/8\); the strict gain is \(1/64\).

## Verification

The accompanying `verify_haldane.py` uses a separately evaluated original two-term response and the product-coordinate rational formula. It tests the derivative identity, exact rational example, random global comparisons over the allocation segment, and two asymptotic laws, using a fixed pseudorandom seed. Its observed output is recorded in `VERIFICATION.md`. Numerical tests are finite and do not replace the universal sign and root arguments above.

## Relationship to prior work

The substrate-inhibited specific-growth mechanism is classical: Andrews (1968) introduced a mathematical model using inhibition to relate microorganism growth and substrate concentration, and Rozich and Gaudy (1984) discussed critical inhibition effects in waste treatment. MacArthur and Pianka (1966) established a classic framework for patch-use optimization. None of those formulations is being claimed as new.

Fazel and Chiang (2005) give general global optimization methods for nonconcave network utilities, including monotone sigmoidal rational examples. Their general method is applicable in principle to nonlinear allocation problems, but the present result is a closed-form, all-parameter classification for the nonmonotone Haldane law, not an assertion of a new general optimizer. Calcagno and coauthors' work (2013, 2014) examines optimal foraging time or movement and the consequences of resource heterogeneity, including type-IV functional responses; these are closely relevant motivations but optimize distinct decision variables. The complete 2014 manuscript was not accessible for direct inspection, so possible unrecognized stronger implications remain a priority risk.

The classification also differs from a two-patch saturating Hill-type allocation result: the latter has monotone single-patch responses and boundary-versus-center global optima, while substrate inhibition here makes boundary allocations strictly suboptimal and creates a center-to-asymmetric-interior transition. Similar mathematical notation or fixed-total constraints alone do not make either result imply the other.

## Limitations

This is an exact theorem only for identical instantaneous Haldane–Andrews response functions with a fixed sum of concentrations, equal positive fixed biomass, and noninteracting compartments. It does not optimize steady-state production, residence times, adaptive resource delivery, stochastic outcomes, general multimodal kinetics, or more than two unequal compartments. The bibliographic assessment does not certify historical novelty; accessible full text could contain an unrecognized special-case formula. The boundary case \(b=0\) is mathematical rather than a finite-parameter physical Haldane reactor.

## References

1. MacArthur, R. H. and Pianka, E. R. (1966), *On Optimal Use of a Patchy Environment*, *The American Naturalist* 100, 603–609, DOI 10.1086/282454. Publisher records first publication on 1966-11-01.
2. Andrews, J. F. (1968), *A mathematical model for the continuous culture of microorganisms utilizing inhibitory substrates*, *Biotechnology and Bioengineering* 10, 707–723, DOI 10.1002/bit.260100602. Publisher records November 1968 without an exact day.
3. Rozich, A. F. and Gaudy, A. F. (1984), *Critical Point Analysis for Toxic Waste Treatment*, *Journal of Environmental Engineering* 110, 562 ff., DOI 10.1061/(ASCE)0733-9372(1984)110:3(562).
4. Fazel, M. and Chiang, M. (2005), *Network Utility Maximization With Nonconcave Utilities Using Sum-of-Squares Method*, Proceedings of the IEEE Conference on Decision and Control, DOI 10.1109/CDC.2005.1582432. Full available manuscript: https://www.princeton.edu/~chiangm/nonconcaveNUM.pdf.
5. Calcagno, V., Mailleret, L., Wajnberg, E. and Grognard, F. (2013), *How optimal foragers should respond to habitat changes: a reanalysis of the Marginal Value Theorem*, *Journal of Mathematical Biology*, DOI 10.1007/s00285-013-0734-y. Online publication 2013.
6. Calcagno, V., Grognard, F., Hamelin, F. M., Wajnberg, E. and Mailleret, L. (2014), *The functional response predicts the effect of resource distribution on the optimal movement rate of consumers*, *Ecology Letters* 17, 1570–1579, DOI 10.1111/ele.12379. Online publication 2014-10-21.
