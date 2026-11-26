# Explicit primitive Frobenius obstructions with a prescribed number of representations

## Finding

Let \(a\ge3\) be an integer and let \(L\ge2\) be even. Define
\[
N=\prod_{j=1}^L(aj-1),\qquad b=\min\{r\ge1:r\equiv-1\pmod a,\ r>N/(aL)\}.
\]
Then \(a,b\) are coprime. The ordinary nonnegative representations of \(N\) by \(a,b\) are exactly the \(L\) pairs
\[
(x_j,y_j)=\left(\frac{N-b(aj-1)}a,\ aj-1\right)\qquad(1\le j\le L),
\]
and their greatest common divisors are exactly \(\gcd(x_j,y_j)=aj-1\). In particular, none is primitive. For each fixed \(a\ge3\) and every prescribed positive even \(L\), the formulas give one missing primitive value with exactly \(L\) ordinary representations and an explicit list of their gcds. The values grow without bound as \(L\) grows. The construction uses an arithmetic-progression product and integer rounding, with no prime search or simultaneous congruence solving.

As a consequence, the largest gap \(g(a,b)\) satisfies
\[
\frac{g(a,b)}{b}\ge \frac{aL}{1+a^2L/N}.
\]
For fixed \(a\ge3\) this tends to infinity along the constructed \(b\)'s. This is an elementary alternative proof of the qualitative unboundedness conclusion, not a new growth theorem: Ding, Wang and Zhang already prove a stronger logarithmic lower bound along a sequence in the same congruence class.

## Assumptions and scope

The generators \(a,b\) are positive and coprime. The coefficients in an ordinary representation \(N=ax+by\) are nonnegative integers and a representation is primitive exactly when \(\gcd(x,y)=1\), with \(\gcd(0,y)=y\) for positive \(y\). The largest missing primitive value \(g(a,b)\) exists by the finiteness theorem for primitive two-generator representations. The construction varies \(b\); it does not prescribe an obstruction with this profile at every fixed pair \((a,b)\).

## Proof

The residue class defining \(b\) makes \(\gcd(a,b)=1\), and the step size of that class is \(a\), so
\[
\frac{N}{aL}<b\le\frac{N}{aL}+a.
\]
In closed form, \(b=a(1+\lfloor (N+aL)/(a^2L)\rfloor)-1\). As \(L\) is even, \(N\equiv1\pmod a\). In any ordinary representation this gives \(y\equiv-1\pmod a\). Together with \(0\le y\le N/b<aL\), it forces \(y=aj-1\) for some \(1\le j\le L\); for each such \(j\) there is at most one possible \(x\).

All \(L\) choices are in fact feasible. If \(L=2\), then \(N=(a-1)(2a-1)\) and \(b=a-1\), so \(N/b=2a-1\). For \(L\ge4\), one has \(N\ge a^3L^2\): at \(L=4\), the inequalities \(aj-1\ge a(3j-1)/3\) give \(N\ge (880/81)a^4>16a^3\). For each subsequent factor, multiplication by \(a(L+1)-1\) more than accounts for the factor \((L+1)^2/L^2\). Consequently,
\[
\frac{N}{aL-1}-\frac{N}{aL}=\frac{N}{aL(aL-1)}\ge a.
\]
It follows that \(b\le N/(aL-1)\), so the largest candidate \(y=aL-1\), and hence every smaller candidate, is feasible. The numerator \(N-by\) is nonnegative and divisible by \(a\) for each candidate.

Finally, \(y=aj-1\) divides \(N\) and is coprime to \(a\). Thus \(y\mid ax=N-by\) forces \(y\mid x\), giving exactly the claimed gcd (including when \(x=0\)). Since \(y\ge a-1\ge2\), no primitive representation exists. In particular \(g(a,b)\ge N\). Dividing the upper bound on \(b\) into \(N\) gives the displayed lower bound. Since \(N\ge(a-1)^L\), \(N/(a^2L)\) and \(b\) both tend to infinity for fixed \(a\).

## Verification

The accompanying `verify.py` is unchanged. It specifies finite exact checks for \(3\le a\le13\) and even \(2\le L\le14\), using integer enumeration of ordinary representations and rational comparison for the lower bound. The finite range gives 77 pairs and 616 representations. The theorem's claim of exactly \(L\) representations and their exact gcds follows from the proof, not extrapolation. For example, \(a=3,L=4\) gives \(N=880,b=74\); the four coefficient pairs are \((244,2),(170,5),(96,8),(22,11)\), with gcds \(2,5,8,11\).

## Relationship to prior work

Ding, Wang and Zhang, [*The Diophantine Frobenius Problem revisited*](https://arxiv.org/abs/2509.08599), Theorem 1.7 and its proof in §4, already obtain an unbounded fixed-generator gap ratio for every \(a>2\). Their proof chooses \(b\equiv-1\pmod a\) and produces missing values of the form \(qab+1\) with \(q\gg_a\log b\), using a suitable prime \(q\) and congruences that ensure a common prime divisor in each candidate representation. That bound is stronger than the asymptotic consequence above. The contribution here is the specific product-and-rounding construction with all the coefficients \(y_j\) dividing \(x_j\), not just with an unspecified common prime divisor; it gives the full gcd list and an elementary witness formula.

Jaffe, [*Denominators in the Farey Sequence, the Stern Sequence, and the Frobenius Problem with Relatively Prime Multipliers*](https://arxiv.org/abs/2610.17267), Theorem 4.3 and Propositions 5.1–5.2, gives finiteness and the linear-size boundary formulas at \(a=1,2\). Thus the qualitative dichotomy in the fixed generator is also prior when combined with Ding, Wang and Zhang. The [uniform primorial construction for two growing generators](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-uniform-primorial-obstructions-for-primitive-two-generator-frobe--0eee43f23b58) requires both generators larger than a growing primorial. A [subsequent fixed-generator primorial construction](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-primorial-obstructions-force-b-log-b-growth-for-primitive-froben--d4c334da51d4) gives a stronger lower bound for all large coprime \(b\), but its obstruction controls a prime divisor of each candidate gcd, not the full profile claimed here.

## Limitations

The theorem determines the representation profile of the displayed missing value, not the exact largest gap \(g(a,b)\), and does not improve the best prior growth bounds. No absolute priority claim is made for product-based divisibility arguments in general.
