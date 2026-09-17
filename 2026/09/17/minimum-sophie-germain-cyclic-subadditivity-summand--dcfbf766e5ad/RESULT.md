# The minimum short summand in a Sophie Germain cyclic subadditivity counterexample is 21

## Context

A positive integer \(r\) is **cyclic** if \(\gcd(r,\varphi(r))=1\), equivalently if every group of order \(r\) is cyclic. Following Cohen, call \(a\) **Sophie Germain cyclic** if both \(a\) and \(2a+1\) are cyclic, and let
\[
C_\sigma(x)=\#\{a\le x: a\text{ is Sophie Germain cyclic}\}.
\]
Cohen conjectured that
\[
C_\sigma(m+n)\le C_\sigma(m)+C_\sigma(n)\qquad(1\le m\le n).
\tag{1}
\]
Ibarra disproved (1) with \((m,n)=(31,3928)\). The result below sharpens the counterexample in a different direction: it determines the smallest possible value of the shorter summand exactly.

## Theorem

If integers \(1\le m\le n\) satisfy
\[
C_\sigma(m+n)>C_\sigma(m)+C_\sigma(n),
\tag{2}
\]
then \(m\ge21\). This bound is sharp: \((m,n)=(21,87088)\) satisfies (2).

Thus **21 is the exact minimum possible smaller summand in any counterexample to Cohen's Sophie Germain cyclic subadditivity conjecture**.

## Proof

### 1. A residue obstruction

Every cyclic integer \(r>2\) is odd. Indeed, \(\varphi(r)\) is even for \(r>2\), so an even \(r\) would have \(\gcd(r,\varphi(r))\ge2\).

Every cyclic integer is also squarefree: if \(p^2\mid r\), then \(p\mid r\) and \(p\mid\varphi(r)\), contradicting \(\gcd(r,\varphi(r))=1\).

Now let \(a>2\) be Sophie Germain cyclic. Since \(a\) is cyclic, it is odd and squarefree, hence \(9\nmid a\). Since \(2a+1\) is cyclic, it is squarefree as well, hence \(9\nmid 2a+1\). The latter condition excludes \(a\equiv4\pmod 9\). Combining oddness with
\[
a\not\equiv0,4\pmod9
\]
gives
\[
a\pmod{18}\in R:=\{1,3,5,7,11,15,17\}.
\tag{3}
\]

For \(m\ge1\), let \(M(m)\) be the maximum number of residues from \(R\) that can occur among \(m\) consecutive integers. Inspecting the 18 possible starting residues modulo 18 gives, for \(m=1,\dots,20\),
\[
M(m)=1,1,2,2,3,3,4,4,5,5,6,6,6,6,7,7,7,7,8,8.
\tag{4}
\]
Meanwhile the Sophie Germain cyclic integers in \([1,21]\) are
\[
1,2,3,5,7,11,15,17,
\]
so for \(m=1,\dots,20\),
\[
C_\sigma(m)=1,2,3,3,4,4,5,5,5,5,6,6,6,6,7,7,8,8,8,8.
\tag{5}
\]
Term by term, (4) is at most (5).

For \(2\le m\le20\) and \(n\ge m\), every integer in the window \((n,n+m]\) is greater than 2. Hence (3)--(5) imply
\[
C_\sigma(n+m)-C_\sigma(n)\le M(m)\le C_\sigma(m),
\]
which is exactly (1). For \(m=1\), the window contains one integer, so its contribution is at most \(1=C_\sigma(1)\). Therefore no counterexample can have \(m\le20\).

### 2. Sharpness at length 21

At length 21 the residue obstruction itself first permits nine candidates: \(M(21)=9\), whereas \(C_\sigma(21)=8\). The window
\[
(87088,87109]
\]
actually realizes nine Sophie Germain cyclic integers:
\[
87089,\ 87091,\ 87095,\ 87099,\ 87101,\ 87103,\ 87105,\ 87107,\ 87109.
\]
Each listed integer \(a\), and each corresponding \(2a+1\), satisfies \(\gcd(r,\varphi(r))=1\); explicit factorizations and gcd certificates are reproduced by `artifacts/verify.py` and recorded in `artifacts/verify-output.txt`.

Consequently
\[
C_\sigma(87109)-C_\sigma(87088)=9>8=C_\sigma(21),
\]
so
\[
C_\sigma(21+87088)>C_\sigma(21)+C_\sigma(87088).
\]
This proves sharpness. \(\square\)

## Significance

Ibarra's counterexample established that Cohen's conjecture is false, using a shorter summand of 31. The theorem above identifies the exact structural boundary: lengths at most 20 are ruled out globally by a congruence-packing obstruction, while length 21 is not merely admissible but is attained by an explicit counterexample.

## Reproducibility

`artifacts/verify.py` uses only the Python standard library. It recomputes:

- the Sophie Germain cyclic integers in \([1,21]\) and the values \(C_\sigma(1),\dots,C_\sigma(21)\);
- the maximum number of allowed residues (3) in every window length \(1,\dots,21\);
- all Sophie Germain cyclic integers in \((87088,87109]\);
- factorizations, Euler totients, and gcd certificates for the nine witness integers and their transforms \(2a+1\).

The lower bound \(m\ge21\) is a mathematical consequence of the residue lemma and the finite table (4); the computation is a reproducibility check for the finite parts, not a substitute for the proof.

## Limitations

Originality is asserted only to the best of our knowledge. The literature search located Cohen's original conjecture, Ibarra's counterexample at \(m=31\), OEIS A397387, and related cyclic-number work, but no source giving the exact minimum smaller summand or the mod-18 obstruction above. A newly posted or poorly indexed follow-up could still overlap this sharpening.

The result minimizes the **smaller summand** \(m\) under the conventional ordering \(m\le n\). It does not minimize \(m+n\), the larger summand \(n\), or the numerical size of a counterexample under another ordering criterion.

## References

1. J. E. Cohen, *Conjectures about Primes and Cyclic Numbers*, Journal of Integer Sequences 28 (2025), Article 25.4.7; arXiv:2508.08335. https://arxiv.org/abs/2508.08335
2. J. A. Ibarra, *A counterexample to a subadditivity conjecture of Cohen for Sophie Germain cyclic numbers*, arXiv:2607.09793 (2026). https://arxiv.org/abs/2607.09793
3. OEIS Foundation Inc., *A397387: Sophie Germain cyclic numbers*. https://oeis.org/A397387
