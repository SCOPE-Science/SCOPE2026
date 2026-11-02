# Exact Gabor stability of every asymmetric two-sided exponential at half-density

## Finding
Fix arbitrary positive real decay rates \(a,b>0\). Define the continuous window
\[
g_{a,b}(t)=\begin{cases}e^{-at},&t\ge0,\\e^{bt},&t<0.\end{cases}
\]
Its Gabor system \(\{e^{2\pi i mt}g_{a,b}(t-n/2):m,n\in\mathbb Z\}\) is a frame of \(L^2(\mathbb R)\). The following are its **optimal squared frame bounds**, without unspecified constants.

Set \(p=e^{-a}\), \(r=e^{-b}\), \(u=(1+p)^{-1}\), \(v=r/(1+r)\), and
\[
\mathcal A=u^2(1+p),\qquad
\mathcal B=uv(1+\sqrt{p/r}),\qquad
\mathcal C=v^2(1+1/r).
\]
Define the positive root and the unique minimizing spatial fiber
\[
t_*={ (b-a)\mathcal B+\sqrt{(a-b)^2\mathcal B^2+4ab\mathcal A\mathcal C}\over 2b\mathcal C},\qquad
x_*={\log t_*\over a+b}\in(0,1/2).
\]
Then the exact optimal lower and upper bounds are
\[
\boxed{A(a,b)=\mathcal A e^{-2ax_*}-2\mathcal B e^{(b-a)x_*}+\mathcal C e^{2bx_*}},
\]
\[
\boxed{B(a,b)=\left({1-pr\over(1-p)(1-r)}\right)^2+
\left({\sqrt p\over1-p}+{\sqrt r\over1-r}\right)^2}.
\]
The least fiber is uniquely attained at modulation phase \(\pi\) and at spatial phase \(x_*\) modulo \(1/2\). The greatest fiber is uniquely attained at modulation phase \(0\) and spatial phase \(0\) modulo \(1/2\). Swapping the two slopes gives \(A(a,b)=A(b,a)\), \(B(a,b)=B(b,a)\), and \(x_*(a,b)+x_*(b,a)=1/2\). Thus the optimum conditioning and the bias of its worst spatial fiber can be computed exactly for every asymmetric choice; no extra frame threshold appears.

## Assumptions and scope
The rates \(a,b\) are arbitrary finite, strictly positive real numbers. The shift lattice is exactly \((1/2)\mathbb Z\) and the modulation lattice exactly \(\mathbb Z\). The window has value \(1\) at zero, with no unit-norm renormalization. A frame bound refers to the coefficients \(\sum_{m,n\in\mathbb Z}|\langle f,e^{2\pi i m(\cdot)}g_{a,b}(\cdot-n/2)\rangle|^2\), comparing with \(\|f\|_2^2\). The formulas do not assert sharp bounds for other lattices or windows.

## Proof
**1. Unit-frequency fiberization.** For \(y\in[0,1]\), \(\theta\in[0,2\pi]\), form the absolutely convergent Zak series
\[
Zg(y,\theta)=\sum_{k\in\mathbb Z}g(y+k)e^{-ik\theta}.
\]
Parseval in the integer modulation index, followed by the unitary Fourier transform in the integer sample index, shows that the Gabor frame quadratic form is multiplication, on \([0,1/2]\times[0,2\pi]\), by
\[
S(x,\theta)=|Zg(x,\theta)|^2+|Zg(x+1/2,\theta)|^2.
\]
Its essential minimum and maximum are the optimal frame bounds. Translation by one changes the Zak transform by a unimodular phase, so \(S\) is periodic in \(x\) with period \(1/2\). Continuity makes essential extrema actual extrema.

**2. Sharp phase reduction.** The geometric series on either side of the kink gives, for \(0\le y\le1\),
\[
Zg(y,\theta)={e^{-ay}\over1-pe^{-i\theta}}+
{r e^{by}e^{i\theta}\over1-re^{i\theta}}
={U_y+V_y e^{i\theta}\over(1-pe^{-i\theta})(1-re^{i\theta})},
\]
where \(U_y=e^{-ay}-pr e^{by}\ge0\) and \(V_y=r(e^{by}-e^{-ay})\ge0\). Both inequalities are strict for interior \(y\). Its squared modulus is the quotient of \(U_y^2+V_y^2+2U_yV_y\cos\theta\) by \((1+p^2-2p\cos\theta)(1+r^2-2r\cos\theta)\). The numerator is nondecreasing in the cosine, while both positive denominator factors are strictly decreasing. Thus \(S\) is strictly increasing in \(\cos\theta\): its phase minimum is at \(\theta=\pi\) and maximum at \(\theta=0\), uniquely modulo \(2\pi\).

**3. Exact maximum.** Write \(P(y)=Zg(y,0)=e^{-ay}/(1-p)+r e^{by}/(1-r)>0\). On \([0,1]\), \(P\) is strictly convex, and so is \(P^2\); therefore \(P(x)^2+P(x+1/2)^2\) is strictly convex on \([0,1/2]\). Its two endpoint values agree because \(P(1)=P(0)\). A strictly convex function with equal endpoint values has its unique global maxima at those endpoints (identified modulo \(1/2\)). Direct substitution of \(P(0)\) and \(P(1/2)\) proves the displayed expression for \(B(a,b)\).

**4. Exact minimum.** Write \(H(y)=Zg(y,\pi)=ue^{-ay}-ve^{by}\). Squaring \(H(x)\) and \(H(x+1/2)\) gives
\[
F(x)=\mathcal A e^{-2ax}-2\mathcal B e^{(b-a)x}+\mathcal C e^{2bx}.
\]
The symmetry of the Zak modulus under integral translation gives \(H(1)=-H(0)\); hence \(F(1/2)=F(0)\). By Rolle's theorem, \(F'\) vanishes at an interior point. Explicit differentiation yields
\[
F'(x)=2e^{-2ax}\left[-a\mathcal A+(a-b)\mathcal B\,t+b\mathcal C\,t^2\right],
\qquad t=e^{(a+b)x}.
\]
The quadratic in brackets has negative constant term and positive leading coefficient. Its roots have opposite signs; it therefore has exactly one positive root \(t_*\), necessarily giving the interior stationary point \(x_*\). As the quadratic crosses from negative to positive at that root, this is the unique minimum in a spatial period. Evaluating \(F(x_*)\) proves the exact lower bound. Positivity is automatic: \(H\) is strictly decreasing and so \(H(x)\), \(H(x+1/2)\) cannot vanish simultaneously. Compactness then gives \(A(a,b)>0\).

**5. Reflection relation.** Since \(g_{b,a}(t)=g_{a,b}(-t)\), reflection is unitary on \(L^2\) and sends the lattice onto itself, preserving both frame bounds. It sends the spatial minimizing fiber \(x_*\) to \(1/2-x_*\), proving the claimed reflection identities by uniqueness.

## Verification
The supplied `check_asymmetric_gabor.py` is a standard-library numerical checker. It computes the closed-form bounds and independently evaluates the exact geometric Zak transform on a two-dimensional phase grid for nine asymmetric and symmetric rate pairs. It verifies both endpoint fibers, the interior critical point, positivity, and reflection identities. Its output was `CHECK_OK: exact geometric Zak fibers, global bounds, internal minimizers and reflection symmetry`. This finite check does not replace the continuous proof above.

## Relationship to prior work
De Dios Pont, Gröchenig, Liehr, Shafkulovska, and Taylor establish the frame-set characterization for continuous integrable totally positive windows, arXiv:2608.04992 (first public August 5, 2026). That theorem implies existence of a positive lower bound for these rate pairs but gives neither of the two exact values above nor the unique biased Zak minimizer. Kloos and Stöckler (arXiv:1311.7359) treat Zak-transform methods and lower estimates for **symmetric** two-sided exponential windows; their section 5 does not supply the asymmetric sharp formulas. Faulhuber and Shafkulovska's 2022 Gabor frame-bound optimization poster gives sharp expressions for the symmetric exponential; that symmetric restriction is subsumed by the displayed formulas but is not independently claimed as new. Janssen's 1996 general frame-bound calculations are pertinent background; the accessible abstract does not resolve whether an implicit specialization gives the asymmetric formula.

## Limitations
The proof covers only the fixed half-translation/integer-modulation lattice and the two-parameter continuous asymmetric exponential profile. It does not classify lattice-optimal configurations or other totally positive windows. Potential implicit historical coverage in generalized Zak-frame calculations, especially Janssen (1996), remains a priority risk. The finite checker is not a numerical proof of the sharp universal bounds.

## References
1. J. de Dios Pont, K. Gröchenig, L. Liehr, I. Shafkulovska, M. A. Taylor, *Gabor Frames of Totally Positive Functions: A Complete Characterization*, arXiv:2608.04992, first public August 5, 2026, https://arxiv.org/pdf/2608.04992 .
2. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359, https://arxiv.org/pdf/1311.7359 .
3. M. Faulhuber and I. Shafkulovska, *Gabor frame bound optimizations*, poster, 2022, https://homepage.univie.ac.at/irina.shafkulovska/wp-content/uploads/2022/07/Strobl-Shafkulovska.pdf .
4. A. J. E. M. Janssen, *Some Weyl-Heisenberg frame bound calculations*, Indagationes Mathematicae 7 (1996), 165–183, DOI:10.1016/0019-3577(96)85088-9 .
