# Sharp affine-slope threshold for fixed-function Möbius primality tests

## Finding

For every nonnegative integer \(c\), define \(f_c(k)=1+c(k-1)\) for \(k\ge1\) and define an integer-valued sequence \(h_c\) by \(h_c(1)=1\) and
\[
h_c(n)=1-n-\sum_{j=2}^{n-1}h_c(j)f_c(\lfloor n/j\rfloor)\qquad(n\ge2).
\]
Then the single fixed function \(f_c\) detects **all and only** primes by the test \(h_c(n)=-1\), for every \(n\ge2\), **if and only if** \(c\ge3\). The threshold is sharp: \(n=4\) is a composite false positive for \(c=0\); \(n=30\) is one for \(c=1\); and \(n=8\) is one for \(c=2\).

More precisely, if \(c\ge3\), then \(h_c(n)\equiv\mu(n)\pmod{c-1}\), and on squarefree integers with exactly \(r\ge1\) prime factors,
\[
h_c(n)=\frac{(-1)^r}{c^2}\sum_{m=1}^{\infty}m^r\left(\frac{c-1}{c}\right)^{m-1}.
\]
This value equals \(-1\) for \(r=1\) and has absolute value strictly larger than \(1\) for every \(r\ge2\).

## Assumptions and scope

The functions \(f_c:\mathbb N\to\mathbb N\) have \(f_c(1)=1\), and the recurrence uniquely determines \(h_c:\mathbb N\to\mathbb Z\) (the codomain of \(h_c\) must allow negative values). The claim concerns **one fixed affine function at a time**, not a polynomial identity quantified over all input functions. The parameter \(c\) is any integer \(c\ge0\), and the primality equivalence is for all integers \(n\ge2\). The symbol \(\mu\) is the classical Möbius function; a squarefree integer has no repeated prime factor. Standard arithmetic-function convolution is \((a*b)(n)=\sum_{d\mid n}a(d)b(n/d)\).

## Proof

**1. Divisor recurrence.** Let \(F_c(n)=\sum_{j=1}^nh_c(j)\). Inserting \(f_c(k)=1+c(k-1)\) into the defining recurrence and using \(h_c(1)=1\) yields, for every \(n\ge2\),
\[
F_c(n)=2-n-c\sum_{j=2}^{n-1}h_c(j)(\lfloor n/j\rfloor-1).
\]
Subtracting the same identity with \(n-1\), and using \(\lfloor n/j\rfloor-\lfloor(n-1)/j\rfloor=1\) precisely when \(j\mid n\), gives
\[
\boxed{h_c(n)=-1-c\sum_{\substack{d\mid n\\1<d<n}}h_c(d).}\tag{1}
\]
For \(n=2\), both sides are \(-1\) directly. Thus (1) is equivalent to the original floor recurrence, not a new definition.

**2. Exclusion of nonsquarefree composites.** Write \(\varepsilon(1)=1\), \(\varepsilon(n)=0\) for \(n>1\), and \(u(n)=1\) for all \(n\). Set \(g_c=\varepsilon+c(u-\varepsilon)\). Equation (1), including the separate value at \(1\), is equivalent to
\[
h_c*g_c=\varepsilon+(c-1)(u-\varepsilon).\tag{2}
\]
If \(c\ge3\), reduce (2) modulo \(c-1\). Since \(g_c\equiv u\pmod{c-1}\), it follows that \(h_c*u\equiv\varepsilon\pmod{c-1}\). Convolve with the classical Möbius inverse \(\mu\) of \(u\) to obtain
\[
\boxed{h_c(n)\equiv\mu(n)\pmod{c-1}}\qquad(n\ge1).\tag{3}
\]
For every nonsquarefree \(n\), \(\mu(n)=0\). Because \(c-1\ge2\), (3) excludes \(h_c(n)=-1\).

**3. Exclusion of squarefree composites.** Suppose \(n\) is squarefree with \(r\) distinct prime factors. The convolution identity (2) restricted to the Boolean lattice of its prime subsets shows that \(h_c(n)\) depends only on \(r\); denote this integer by \(H_{c,r}\), with \(H_{c,0}=1\). The exponential generating functions of the three terms in (2) are respectively
\[
H_c(z)=\sum_{r\ge0}H_{c,r}\frac{z^r}{r!},\quad
G_c(z)=ce^z-(c-1),\quad
K_c(z)=(c-1)e^z-(c-2).
\]
Their Boolean subset convolution becomes multiplication: \(H_c(z)G_c(z)=K_c(z)\). Hence for \(c\ge3\), with \(\rho=(c-1)/c\in(0,1)\),
\[
H_c(z)=1-\frac1c+\frac1{c^2}\frac{e^{-z}}{1-\rho e^{-z}}.
\]
The latter has a convergent analytic expansion near \(z=0\), namely \(c^{-2}\sum_{m\ge1}\rho^{m-1}e^{-mz}\) for the nonconstant part. Taking its \(r\)-th derivative at zero proves the displayed squarefree formula for \(r\ge1\). Since \(\sum_{m\ge1}m\rho^{m-1}=(1-\rho)^{-2}=c^2\), we have \(H_{c,1}=-1\). If \(r\ge2\), then \(m^r\ge m\) for all \(m\ge1\), strictly for \(m\ge2\), with positive weights. Consequently \(|H_{c,r}|>1\), so no squarefree composite passes.

**4. All primes and sharpness.** If \(n\) is prime, the proper-divisor sum in (1) is empty and \(h_c(n)=-1\), for **every** \(c\ge0\). If \(c=0\), (1) gives \(h_0(n)=-1\) for all \(n\ge2\), including \(4\). If \(c=1\), (2) reduces to \(h_1*u=\varepsilon\), so \(h_1=\mu\), and the squarefree composite \(30=2\cdot3\cdot5\) has value \(-1\). Finally, applying (1) to prime powers inductively yields
\[
h_c(p^a)=-(1-c)^{a-1}\qquad(a\ge1).
\]
In particular, \(h_2(8)=-(1-2)^2=-1\). Thus no slope below \(3\) works, while every slope at least \(3\) does. \(\square\)

## Verification

The accompanying standalone `verify.py` recomputes the original floor recurrence and divisor recurrence independently for all integral slopes \(0\le c\le8\), comparing values through \(n=240\). It checks the congruence (3), every prime/composite classification through \(n=2500\), the squarefree Boolean-subset formulas where the test integer lies in range, prime-power formulas, and all three sharpness counterexamples. Run `python verify.py` with the Python 3 standard library. The tests passed in this package. The proof above, not finite enumeration, establishes the assertions for all stated parameters.

## Relationship to prior work

Andrews, Kauffman and Sahoo introduced the generalized floor recurrence and proved its divisor reformulation in their September 2026 paper. Their Theorem 1 is stated as a primality biconditional for arbitrary functions, but their composite-case argument establishes nonidentity **across all choices of the function**; that does not establish a biconditional for an **individual fixed function**. A separately published constant-function obstruction exhibits the same quantifier distinction. Here the affine subfamily is classified completely: the tests do work for all slopes \(c\ge3\), but fail for exactly the three smaller nonnegative integral slopes. The proof combines the established divisor reformulation with a Dirichlet-convolution congruence and an exact squarefree exponential generating function. Classical Möbius inversion supplies the standard algebraic identity; it does not by itself state the affine threshold.

## Limitations

Only nonnegative **integer** slopes are classified; nonintegral, negative, and nonaffine choices of \(f\) are not covered. The result is an exact arithmetic characterization, not an assertion about the running-time efficiency of a primality algorithm. A general formula for \(h_c(n)\) on arbitrary nonsquarefree integers is not required. Overlap checks considered the primary 2026 paper, available public mathematical-result records and accessible literature, but cannot rule out an earlier implicit equivalent in general Dirichlet-inverse theory. No independent audit has been performed.

## References

1. G. E. Andrews, L. H. Kauffman and D. Sahoo, *A surprising generalization of the Möbius function*, arXiv:2609.25628v1 (first publicly available 2026-09-22), Sections 1–2, especially Proposition 1 and Theorem 1.
2. *A constant-function obstruction to a generalized Möbius primality criterion*, published-finding corpus research record `published-finding corpus public finding: A constant-function obstruction to a generalized Möbius primality criterion (2026-10-04)` (public mathematical-result summary; full record was not inspected).
3. Classical Möbius inversion on the divisor lattice; used here only in the standard identity \(\mu*u=\varepsilon\).
