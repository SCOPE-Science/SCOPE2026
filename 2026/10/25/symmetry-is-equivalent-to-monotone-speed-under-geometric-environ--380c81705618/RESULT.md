# Symmetry is equivalent to monotone speed under geometric environmental refresh

## Finding

Let a nearest-neighbor random walk on \(\mathbb Z\) use i.i.d. site transition probabilities \(\omega_x\), with a complete, independent resampling of the entire environment after each step with probability \(p\). Suppose that \(\omega_x\in[\delta,1-\delta]\) almost surely for some \(\delta>0\) and \(\mathbb E\omega_x=1/2\). Let \(v(p)\) denote its annealed almost-sure limiting velocity, including the static case \(p=0\).

The following conditions are equivalent:

1. The one-site law of \(\omega_x\) is invariant under \(\omega_x\mapsto1-\omega_x\).
2. \(v(p)=0\) for every \(p\in[0,1]\).
3. \(p\mapsto v(p)\) is monotone on \([0,1]\) (in either direction).

More quantitatively, let \(Y=\omega_x-1/2\), and suppose that for an integer \(r\ge1\),
\[\mathbb E[Y^3]=\mathbb E[Y^5]=\cdots=\mathbb E[Y^{2r-1}]=0,\qquad m_{2r+1}:=\mathbb E[Y^{2r+1}]\ne0.\]
For two independent copies \(Y_1,Y_2\) of \(Y\), the first nonzero term of the velocity at complete refresh is
\[\boxed{v(p)=2m_{2r+1}\,\mathbb E[(Y_1+Y_2)^{2r}](1-p)^{4r}+O((1-p)^{4r+1})\quad(p\uparrow1).}\]
The even-moment factor is strictly positive. For \(r=1\) this coefficient is \(4\mathbb E[Y^2]\mathbb E[Y^3]\); if the third central moment vanishes but the fifth does not, the \(r=2\) coefficient is \(4\mathbb E[Y^5](\mathbb E[Y^4]+3(\mathbb E[Y^2])^2)\). Thus *every* non-reflection-symmetric mean-balanced site law produces nonzero velocity for sufficiently frequent but imperfect refresh, even though both \(v(0)\) and \(v(1)\) are zero. Its velocity curve is necessarily nonmonotone. The exponent \(4r\) is sharp for each first nonzero odd central moment.

## Assumptions and scope

The environments \(\omega^{(j)}=(\omega^{(j)}_x)_{x\in\mathbb Z}\) are mutually independent, and their site entries are i.i.d. with common law \(\mu\) supported in \([\delta,1-\delta]\). At site \(x\), the walker moves right with probability \(\omega^{(j)}_x\) and left with probability \(1-\omega^{(j)}_x\) until a global environment resampling occurs. After every step a fresh complete environment is selected with probability \(p\in(0,1]\), independently of other randomness; waiting times between selections are geometric with parameter \(p\). At \(p=0\), one environment is fixed forever. The walker starts at zero.

All expectations for a fixed, unrefreshed environment averaged over its randomness are *annealed*. Write \(Z_n\) for the static-environment walk started at zero, and \(a_n=\mathbb E Z_n\). The strong law for independent geometric regeneration blocks defines \(v(p)\) for \(p>0\); the classical one-dimensional static random-environment law defines \(v(0)\). The parameter \(r\) is finite exactly when the centered one-site distribution is asymmetric; the case of symmetric distributions is handled separately.

## Proof

**1. Regeneration identity and endpoint velocities.** For \(0<p\le1\), a geometric regeneration block has length \(L\) with \(\mathbb P(L=n)=p(1-p)^{n-1}\). Its annealed displacement has mean \(\sum_{n\ge1}p(1-p)^{n-1}a_n\), and its mean duration is \(1/p\). The independent-block strong law gives
\[v(p)=p^2\sum_{n\ge1}a_n(1-p)^{n-1}.\tag{1}\]
Since \(|a_n|\le n\), this is analytic for \(|1-p|<1\) and the remainder after any finite truncation is controlled. At \(p=1\), the right-step probability is \(\mathbb E\omega_x=1/2\), hence \(v(1)=0\). For the static walk put \(\rho=(1-\omega_x)/\omega_x\). Jensen's inequality yields
\[\mathbb E\rho=\mathbb E(1/\omega_x)-1\ge1,\qquad \mathbb E(\rho^{-1})=\mathbb E(1/(1-\omega_x))-1\ge1.\]
The one-dimensional i.i.d. random-environment speed criterion of Solomon (restated in Avena et al., Proposition 1.3, with its reflected counterpart) therefore gives \(v(0)=0\). Continuity of \(v\) at zero follows from Martin and Nagel's regeneration theorem, or its block representation and the static speed limit.

**2. Cancellation before the first odd-moment signal.** Denote the reflection of \(\mu\) under \(\omega\mapsto1-\omega\) by \(\mu^\ast\). Reflecting every spatial location and every step reverses the displacement distribution, so \(a_n(\mu^\ast)=-a_n(\mu)\). Under the displayed moment hypotheses the centered laws of \(\mu\) and \(\mu^\ast\) have equal moments through degree \(2r\). The probability of any fixed nearest-neighbor path of length \(n\) is a product, over sites, of terms \(\mathbb E[\omega^u(1-\omega)^w]\), where \(u+w\) is the number of departures from that site. Departures from the same site are separated by at least two steps, so for \(n\le4r\) every term has degree at most \(2r\). Thus the entire annealed \(n\)-step path law is identical for \(\mu\) and \(\mu^\ast\); reflection then forces
\[a_1=a_2=\cdots=a_{4r}=0.\tag{2}\]

**3. Exact first signal.** Because \(a_{4r}=0\), the expected displacement at step \(4r+1\) is the annealed expectation of the final local drift \(2\omega_{Z_{4r}}-1\). In a length-\(4r\) history, the corresponding expectation uses centered moments of degree at most \(2r\) at every site, except when the terminal site was departed from exactly \(2r\) times. This exception can occur only at the starting site, with the walk making precisely \(2r\) consecutive two-step excursions \(0\to\pm1\to0\). All other histories have identical contributions under \(\mu\) and \(\mu^\ast\), while spatial reflection changes their aggregate sign; their aggregate is therefore zero.

For the exceptional histories, sum over the two choices of excursion at every return. With independent variables \(\omega_0,\omega_{-1},\omega_1\) from \(\mu\), their total expected final drift equals
\[T=\mathbb E\left[(2\omega_0-1)\left\{\omega_0(1-\omega_1)+(1-\omega_0)\omega_{-1}\right\}^{2r}\right].\tag{3}\]
Put \(Y_0=\omega_0-1/2\), \(A=1-\omega_1\), \(B=\omega_{-1}\), \(C=(A+B)/2\), and \(D=A-B\). The term in braces is \(C+Y_0D\). Since \(A\) and \(B\) are independent and have matching moments through degree \(2r\), the expectation of \(C^{2r-k}D^k\) vanishes for odd \(k\le2r\) by exchange symmetry of moments. For even \(k<2r\), \(\mathbb E Y_0^{k+1}=0\) by hypothesis. Expanding (3) therefore leaves the single term \(k=2r\):
\[a_{4r+1}=T=2m_{2r+1}\,\mathbb E[D^{2r}]=2m_{2r+1}\,\mathbb E[(Y_1+Y_2)^{2r}].\tag{4}\]
This last moment is strictly positive when \(m_{2r+1}\ne0\), because then \(Y\) is nondegenerate and the sum of two independent copies is nondegenerate. Substituting (2)–(4) into (1), and bounding the remaining series using \(|a_n|\le n\), proves the stated expansion.

**4. Equivalence.** Reflection invariance of \(\mu\) makes each annealed finite-time displacement symmetric, so (1) gives \(v\equiv0\); hence the speed is monotone. Conversely, the endpoint calculation gives \(v(0)=v(1)=0\), so a monotone velocity curve must be identically zero. If \(\mu\ne\mu^\ast\), compact-support moment determinacy gives a first nonzero odd centered moment of order \(2r+1\ge3\). Its strictly nonzero coefficient (4) makes \(v(p)\ne0\) near \(p=1\), contradicting identically zero speed. This proves all three equivalences.

For concreteness, the law \(\mathbb P(\omega=1/4)=3/5\), \(\mathbb P(\omega=7/8)=2/5\) has mean \(1/2\), centered variance \(3/32\), and centered third moment \(3/256\). Thus
\[v(p)=\frac{9}{2048}(1-p)^4+O((1-p)^5),\qquad v(0)=v(1)=0.\]
Its positive interior velocity is not merely formal: at \(p=9999/10000\), (1) and \(|a_n|\le n\) give a strictly positive lower bound \(p^2(1-p)^4\left(9/2048-(1-p)(6-5(1-p))/p^2\right)>0\).

## Verification

The independent exact-rational checker `verify_regenerating_symmetry.py` enumerates static-walk path probabilities, first checking the skewed two-atom example through five steps. It also uses a four-atom mean-balanced law with zero third centered moment but nonzero fifth centered moment and verifies the predicted order-eight coefficient by enumerating paths through nine steps. Symmetric two-atom controls have zero annealed displacement at every tested length. Run with `python verify_regenerating_symmetry.py`; no third-party packages are required. These finite tests are checks of the first two instances, not a substitute for the all-order reflection and excursion proof.

## Relationship to prior work

Martin and Nagel (arXiv:2610.11919v1, first public October 8, 2026) derive the geometric-regeneration speed representation (1), its analyticity, and low-order derivatives at complete refresh. In particular, their second derivative is proportional to the mean single-step drift and hence vanishes in the mean-balanced case. They also provide nonmonotone examples with nonzero mean single-step drift. The new assertion here is the all-order moment-triangular identity (2)–(4), the exact symmetry-versus-zero-velocity classification, and the forced nonmonotonicity of *every* asymmetric mean-balanced site law. Their representation is a key input, not a new claim here; the classification does not follow merely by substituting the mean into their displayed derivative formulas.

Solomon's static speed criterion supplies the endpoint equality \(v(0)=0\). Avena, Chino, da Costa, and den Hollander study deterministic cooling times and reproduce that static criterion; their cooling theory is distinct from fixed geometric refresh. These classical ingredients are credited and are not claimed as original.

## Limitations

This result assumes independent spatial site probabilities, independent *complete* geometric environmental resampling, nearest-neighbor motion, uniform ellipticity, and mean site probability \(1/2\). It does not cover partial spatial refresh, dependent site environments, arbitrary renewal distributions, or mean-biased laws. The asymptotic sign is asserted only sufficiently near full refresh, not for every interior value of \(p\). The result does not identify the number or location of interior velocity extrema. An implicit equivalent theorem in the broader random-environment literature remains a residual originality risk.

## References

1. R. Martin and J. Nagel, *Random walk in a regenerating random environment*, arXiv:2610.11919v1, October 8, 2026, https://arxiv.org/html/2610.11919v1 .
2. L. Avena, Y. Chino, C. da Costa, and F. den Hollander, *Random walk in cooling random environment: ergodic limits and concentration inequalities*, arXiv:1803.03295, first submitted March 8, 2018, https://arxiv.org/abs/1803.03295 .
3. F. Solomon, *Random walks in a random environment*, Annals of Probability 3 (1975), 1–31; see the speed criterion restated in reference 2, Proposition 1.3.
