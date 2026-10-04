# Review: Superharmonic numbers with prime odd part are even perfect

## Correctness
PASS. For \(n=2^a p\), writing \(A=a+1\) gives \(\tau(n)=2A\) and \(\sigma(n)=(2^A-1)(p+1)\). Cohen's necessary valuation criterion first forces every prime divisor of \(2^A-1\) to equal \(p\): if another prime \(r\) occurred, then \(r\mid A\), while lifting the exponent gives \(v_r(2^A-1)\ge v_r(A)+1\), contradicting the required valuation bound. Thus \(2^A-1=p^c\). A second order/LTE argument shows \(\operatorname{ord}_p(2)=A\). Any odd prime divisor of \(p+1\) would then divide both \(A\) and \(p-1\), impossible, so \(p+1\) is a power of \(2\). Primality of \(p\) then identifies that exponent with \(A\), forcing \(c=1\). The converse is the Euclid–Euler even-perfect form. The finite checker independently confirms the defining divisibility on the stated bounded domain.

## Originality
PASS with a residual bibliographic risk only. Cohen's foundational full text explicitly says that the harmonic two-prime classification does not carry through to superharmonic numbers, although it appears likely to remain true; it does not isolate or prove the prime-odd-part slice. Pollack–Pomerance later sharpen global counting bounds and study narrower prime-perfect/prime-deficient conditions, but do not supply this structural converse. Targeted searches for superharmonic \(2^a p\), prime odd part, squarefree odd part, and the two-prime conjecture found no equivalent or stronger statement. The closest indexed research result concerns proper power-harmonic numbers, a different divisor-sum notion.

## Value
PASS. The result closes an infinite, canonical first slice of the explicit two-distinct-prime-factor question raised in the foundational superharmonic paper. The squarefree odd-part case is not an arbitrary cutoff: it is the minimal two-prime layer in which the odd component contributes no extra exponent factor to \(\tau(n)\). The proof also explains structurally why the enlarged superharmonic divisibility condition collapses back to ordinary harmonicity in this slice.

## Closest literature and limitations
The primary source is Cohen's 2008 electronically published paper, especially Theorem 1 and the paragraph immediately following it. Pollack–Pomerance's 2012 paper was checked for later superharmonic developments; its Section 5.2 strengthens density bounds and discusses prime-deficient numbers, but does not classify the present family. The theorem leaves open odd-prime exponents greater than one and therefore does not settle the full two-prime question.

Same-model review: passed. Independent audit: not yet performed.
