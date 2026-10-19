# Exact Abelian-border spectra of Christoffel conjugates

## Finding

Fix integers \(n\ge 2\) and \(1\le b<n\) with \(\gcd(n,b)=1\). Define the lower binary Christoffel word \(w=w_0\cdots w_{n-1}\) by
\[
w_i=\left\lfloor\frac{(i+1)b}{n}\right\rfloor-\left\lfloor\frac{ib}{n}\right\rfloor\quad(0\le i<n).
\]
For each \(s\in\{0,\ldots,n-1\}\), let \(w^{(s)}=w_s\cdots w_{n-1}w_0\cdots w_{s-1}\), and let \(\mathcal B_s\subseteq\{1,\ldots,n-1\}\) consist of lengths \(\ell\) for which its prefix and suffix of length \(\ell\) have the same number of each binary symbol (an Abelian border). Put \(j_s\equiv sb\pmod n\), \(0\le j_s<n\), and \(r_\ell\equiv \ell b\pmod n\), \(1\le r_\ell<n\). Then the **entire proper Abelian-border set** is
\[
\mathcal B_s=\left\{\ell:1\le r_\ell\le\min(j_s,n-1-j_s)\right\}
\cup\left\{\ell:\max(j_s,n-1-j_s)<r_\ell\le n-1\right\}.
\]
In particular,
\[
\boxed{|\mathcal B_s|=2\min(j_s,n-1-j_s).}
\]
As \(s\) runs through all \(n\) conjugates, this multiset of counts is **independent of the coprime slope** \(b/n\). More explicitly, for \(n=2m\), each of \(0,2,\ldots,2m-2\) occurs exactly twice. For \(n=2m+1\), each of \(0,2,\ldots,2m-2\) occurs exactly twice, and \(2m\) occurs exactly once. Thus exactly two conjugates have no Abelian border; when \(n\) is odd there is exactly one conjugate in which every proper length is an Abelian border.

## Assumptions and scope

Words are finite, linear, indexed from zero, over the **fixed labeled binary alphabet** \(\{0,1\}\). Conjugacy means cyclic rotation of the length-\(n\) word. A proper Abelian border length is any integer \(1\le\ell<n\) whose length-\(\ell\) prefix and suffix have equal Parikh vectors; overlaps are permitted. The claim assumes \(\gcd(n,b)=1\), so the Christoffel word is primitive and each nonzero residue \(r_\ell\) appears exactly once as \(\ell\) varies through \(1,\ldots,n-1\). Both boundary lengths \(n=2\) and slopes \(b=1\), \(b=n-1\) are included. No assertion is made for noncoprime parameters, larger alphabets, or non-Christoffel words.

## Proof

Extend \(w_i\) to every integer \(i\) by the same floor-difference formula. It is \(n\)-periodic because shifting \(i\) by \(n\) increases each argument of each floor by the integer \(b\).

Fix \(s\) and \(1\le\ell<n\). The number of ones in the length-\(\ell\) prefix of \(w^{(s)}\), interpreted in this periodic extension, telescopes to
\[
P=\left\lfloor\frac{(s+\ell)b}{n}\right\rfloor-\left\lfloor\frac{sb}{n}\right\rfloor.
\]
The number of ones in its suffix is equal to the number in the preceding cyclic interval of length \(\ell\):
\[
Q=\left\lfloor\frac{sb}{n}\right\rfloor-\left\lfloor\frac{(s-\ell)b}{n}\right\rfloor.
\]
Write \(sb=un+j_s\) and \(\ell b=vn+r_\ell\), with integers \(u,v\) and residues satisfying \(0\le j_s<n\), \(1\le r_\ell<n\). Elementary floor arithmetic gives
\[
P=v+\mathbf1_{\{j_s+r_\ell\ge n\}},\qquad
Q=v+\mathbf1_{\{r_\ell>j_s\}}.
\]
Since prefix and suffix have the same length, their complete binary Parikh vectors agree exactly when \(P=Q\). The two indicators are both zero precisely when \(r_\ell\le j_s\) and \(r_\ell<n-j_s\), equivalently \(1\le r_\ell\le\min(j_s,n-1-j_s)\). They are both one precisely when \(r_\ell>j_s\) and \(r_\ell\ge n-j_s\), equivalently \(\max(j_s,n-1-j_s)<r_\ell\le n-1\). These are disjoint intervals, each containing \(\min(j_s,n-1-j_s)\) positive residues. This proves the exact border-set formula.

Because multiplication by the coprime integer \(b\) permutes all nonzero residue classes modulo \(n\), precisely \(2\min(j_s,n-1-j_s)\) lengths meet the formula. Multiplication by \(b\) also permutes the rotation indices \(s\) into the complete list of residues \(j_s=0,\ldots,n-1\). When \(n=2m\), the minimum of \(j\) and \(2m-1-j\) takes each value \(0,\ldots,m-1\) twice. When \(n=2m+1\), the minimum of \(j\) and \(2m-j\) takes each value \(0,\ldots,m-1\) twice and \(m\) once. This proves both distributions and all asserted extremal multiplicities.

For odd \(n\), the unique rotation with \(j_s=(n-1)/2\) has every proper Abelian border. In fact it is a palindrome: writing the equality of prefix and suffix symbol counts for successive lengths and subtracting forces the symbols at symmetric positions to coincide. This independently recovers the known odd-length palindromic conjugate phenomenon, but the full border-count spectrum is a different invariant.

## Verification

The standalone `check.py` independently constructs mechanical words and enumerates **every** prefix/suffix Parikh equality for all coprime pairs \((n,b)\) with \(2\le n\le80\), every rotation, and every proper border length. It checks the exact residue characterization, the per-rotation count, and the multiset of counts. Running `python check.py` produces:

`PASS_CHRISTOFFEL_ABELIAN_BORDER n=2..80 coprime_length_slope_pairs=1965 rotations=105388 border_decisions=6250510`

These finite comparisons corroborate boundary conventions and computations; the theorem for arbitrary \(n\) follows solely from the preceding integer-floor proof.

## Relationship to prior work

Blanchet-Sadri, Chen, and Hawes (2017) count all binary words by their numbers of Abelian borders, via lattice paths (Theorem 3), without conditioning on Christoffel conjugacy classes or tracking individual rotations. Carey and Clampitt (2018) classify height profiles of **shorter-than-full-length circular factors** of Christoffel words for fixed ordered partitions; their results concern distributions of varieties at a fixed factor length, not the joint set of equal Parikh prefix/suffix lengths in each full-length rotation. Bugeaud and Reutenauer (first public preprint 2022) describe **ordinary exact-match borders** and palindromic conjugates of Christoffel words. Their ordinary-border descriptions do not determine the Abelian-border spectrum: equal Parikh vectors are strictly weaker than identical strings. The formula here is a new targeted comparison of two complementary cyclic windows simultaneously across all proper lengths and rotations, not a rephrasing of any of those stated theorems.

## Limitations

The scope is restricted to primitive binary lower Christoffel words and their rotations. The theorem does not classify Abelian borders for arbitrary balanced binary words, nonprimitive mechanical words, or alphabet sizes greater than two. The literature comparison found no explicit identical spectrum statement in the accessed sources; a differently presented or unindexed equivalent may exist. No independent mathematical audit has been carried out.

## References

1. F. Blanchet-Sadri, K. Chen, K. Hawes, *Dyck Words, Lattice Paths, and Abelian Borders*, first public arXiv version 2017-08-22, arXiv:1708.06461, https://arxiv.org/abs/1708.06461 .
2. N. Carey, D. Clampitt, *Partitioned Factors in Christoffel and Sturmian Words*, first public arXiv version 2018-04-23, arXiv:1804.08724, https://arxiv.org/abs/1804.08724 .
3. Y. Bugeaud, C. Reutenauer, *On the conjugates of Christoffel words*, first public arXiv version 2022-02-11, arXiv:2202.05486, https://arxiv.org/abs/2202.05486 .
