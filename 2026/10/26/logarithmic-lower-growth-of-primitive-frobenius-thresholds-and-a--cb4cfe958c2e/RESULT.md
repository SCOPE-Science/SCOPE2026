# Logarithmic lower growth of primitive Frobenius thresholds and a sharp boundary at two

## Finding

For coprime integers \(a,b\ge2\), define the primitive Frobenius number \(g(a,b)\) to be the largest integer \(n\ge0\) for which there do **not** exist \(x,y\in\mathbb Z_{\ge0}\) with \(ax+by=n\) and \(\gcd(x,y)=1\). Its finiteness is established by Jaffe (2026, Theorem 4.3).

For integers \(a\ge3\) and \(R\ge2\), put
\[Q_a(R)=\prod_{\substack{p\le R\\p\text{ prime},\ p\nmid a}}p.\]
If \(b>aQ_a(R)\) and \(\gcd(a,b)=1\), then there is an integer \(n\) with
\[Rb<n<(R+1)b\]
which has no primitive nonnegative representation \(ax+by=n\). In particular, \(g(a,b)>Rb\). Thus for each fixed \(a\ge3\),
\[\boxed{\liminf_{\substack{b\to\infty\\\gcd(a,b)=1}}\frac{g(a,b)}{b\log b}\ge1.}\]
For the boundary coefficient \(a=2\), every odd integer \(b\ge3\) satisfies the exact formula
\[\boxed{g(2,b)=4b-2.}\]
Consequently the normalized threshold stays bounded for \(a=2\), whereas it diverges at least logarithmically for every fixed \(a\ge3\).

## Assumptions and scope

The integers \(a,b\) are both at least two and are coprime. In the primorial obstruction \(a\ge3\), \(R\ge2\) is integral, and no primality condition is imposed on \(b\). All logarithms are natural. The liminf is taken only through positive integers \(b\) coprime to the specified fixed \(a\). The construction and the claim are deterministic, not probabilistic.

## Proof

**Finite primorial obstruction.** Fix \(a\ge3\), \(R\ge2\), and admissible \(b>aQ_a(R)\). Write \(Q=Q_a(R)\); then \(\gcd(Q,a)=1\). Because \(\varphi(a)\ge2\), we can select a unit residue class \(c\pmod a\) different from \(b\pmod a\). The Chinese remainder theorem supplies one integer congruence class modulo \(aQ\) satisfying \(n\equiv0\pmod Q\) and \(n\equiv c\pmod a\). The open interval \((Rb,(R+1)b)\) has length \(b>aQ\), so it contains an integer \(n\) in that congruence class.

Suppose \(n=ax+by\) for some nonnegative integers \(x,y\). Since \(n\) and \(b\) are both coprime to \(a\), the congruence \(by\equiv n\pmod a\) implies \(\gcd(y,a)=1\). The choice \(n\not\equiv b\pmod a\) rules out \(y=1\); it also rules out \(y=0\), since \(n\) is a unit modulo \(a\). The strict inequality \(n<(R+1)b\) yields \(2\le y\le R\). Choose any prime \(p\mid y\). It satisfies \(p\le R\) and \(p\nmid a\), hence \(p\mid Q\mid n\). Because \(p\mid by\), the equality \(ax=n-by\) gives \(p\mid ax\), and \(p\nmid a\) forces \(p\mid x\). Therefore \(\gcd(x,y)\ge p>1\). No primitive representation exists, proving \(g(a,b)\ge n>Rb\).

**Asymptotic consequence.** With \(a\) fixed and \(R\to\infty\), the prime number theorem gives
\[\log Q_a(R)=\sum_{p\le R}\log p-\sum_{p\mid a,\,p\le R}\log p=R+o(R).\]
For any fixed \(0<\varepsilon<1\), set \(R=\lfloor(1-\varepsilon)\log b\rfloor\). Then \(aQ_a(R)<b\) for all sufficiently large coprime \(b\), and the construction gives \(g(a,b)>Rb\). Dividing by \(b\log b\), taking the liminf, then letting \(\varepsilon\downarrow0\), proves the asserted constant-one lower bound. No uniformity in \(a\) is claimed.

**Boundary at two.** Let \(b\ge3\) be odd and put \(n_0=4b-2\). If \(2x+by=n_0\) with \(x,y\ge0\), then \(y\in\{0,2\}\). For \(y=0\), \(x=2b-1\), while for \(y=2\), \(x=b-1\); neither pair is coprime. Thus \(g(2,b)\ge4b-2\). Every integer \(n\ge4b-1\) is primitively represented: for odd \(n\), take \(y=1\) and \(x=(n-b)/2\); for \(n\equiv0\pmod4\), take \(y=2\) and \(x=n/2-b\), which is odd; and for \(n\equiv2\pmod4\), take \(y=4\) and \(x=n/2-2b\), which is odd. Each \(x\) is nonnegative in its indicated range. The three cases prove \(g(2,b)=4b-2\).

## Verification

Run `python3 verify.py` with Python 3.8 or later; it independently enumerates all nonnegative solutions at explicitly constructed obstructed values for 50 cases with \(3\le a\le12\) and \(R\in\{2,3,5,7,11\}\), and independently checks the exact boundary formula for 50 odd values of \(b\). Expected final line: `CERTIFICATE_OK primorial_obstructions=50 exact_boundary_cases=50`. These finite computations are corroboration, not the basis for the infinite proof. No unproved numerical extrapolation is used.

## Relationship to prior work

Jaffe's public 2026 treatment of Stern/Farey denominators and coprime-multiplier Frobenius numbers proves finiteness, supplies effective upper bounds, and gives the fixed-coefficient experimental graphs and conjectures motivating the present question. The present result instead provides an explicit **lower** obstruction valid for every sufficiently large coprime \(b\), establishes at least logarithmic growth with leading lower constant one when \(a\ge3\), and resolves the exact \(a=2\) boundary. The underlying 2026 article identifies a 2023 dissertation as antecedent work; this earlier context must be distinguished from the date of the cited arXiv version. Classical prime-product and Chinese-remainder ingredients are not claimed as novel individually. Earlier implicit treatments of these lower bounds cannot be completely ruled out.

## Limitations

The lower asymptotic constant is not shown optimal; no asymptotic equality or upper bound of comparable order is proved. The finite obstruction requires \(b>aQ_a(R)\), which is numerically large. The asymptotic depends on the standard prime number theorem. It does not apply uniformly when \(a\) increases with \(b\). Scientific originality awaits independent literature review; the separately published 2023 dissertation was available by abstract, but its full text was not accessible in the present comparison.

## References

1. G. N. Jaffe, *Denominators in the Farey Sequence, the Stern Sequence, and the Frobenius Problem with Relatively Prime Multipliers*, arXiv:2610.17267v1 (first posted 2026-10-12), https://arxiv.org/abs/2610.17267 .
2. G. N. Jaffe, *Topics in Analytic Number Theory*, Ph.D. dissertation, University of Illinois (public record dated 2023-04-28), https://hdl.handle.net/2142/120085 .
3. Prime number theorem in the equivalent Chebyshev-theta formulation \(\sum_{p\le x}\log p=x+o(x)\) (classical).
