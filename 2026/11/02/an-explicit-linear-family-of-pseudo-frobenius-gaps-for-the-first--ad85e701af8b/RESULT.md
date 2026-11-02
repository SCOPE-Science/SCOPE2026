# An explicit linear family of pseudo-Frobenius gaps for the first three-bit Proth semigroups

## Finding
For every integer \(n\ge3\), put \(B=2^n\), \(A=7B\), and
\[
 S_n=\langle 7\cdot 2^{n+i}+1:i\in\mathbb Z_{\ge0}\rangle,\quad m=A+1.
\]
For \(0\le t\le A\), define \(\lambda(t)\) to be the smallest number of coins in a representation of \(t\) by positive denominations \(c_j=2^j-1\), \(j\ge1\), with \(\lambda(0)=0\). Define
\[
 p(t)=At+(A+1)\lambda(t)-(A+1).
\]
Every element in the following explicitly indexed set is a pseudo-Frobenius number of \(S_n\):
\[
 \mathcal P_n=\{p(4B-n-2),\ p(6B-n-2),\ p(A),\ p(A-1)\}
 \cup\{p(A-d):5\le d\le n+2\}.
\]
All the indices are distinct. Hence \(\#\mathcal P_n=n+2\) and the type \(\#\operatorname{PF}(S_n)\ge n+2\). More explicitly, the two isolated members are \(p(4B-n-2)=A(4B-n-2)+(A+1)(n+1)\) and \(p(6B-n-2)=A(6B-n-2)+(A+1)(n+1)\); the remaining members are \(p(A)=A^2+3A+3\), \(p(A-1)=A^2+3A+4\), and \(p(A-d)=A^2-A+d-1\) for \(5\le d\le n+2\).

## Assumptions and scope
Here \(n\) is any integer at least three, all semigroup coefficients are nonnegative integers, and the pseudo-Frobenius set is \(\operatorname{PF}(S)=\{f\notin S:f+s\in S\ \forall s\in S\setminus\{0\}\}\). No assertion is made that the displayed subset exhausts the pseudo-Frobenius set or that the lower bound is sharp for every \(n\).

## Proof
**1. Apéry coordinates.** The positive generators are \(m=A+1\) and \(g_j=A2^j+1=Ac_j+m\) for \(j\ge1\). For each \(0\le t\le A\) let \(w(t)=At+m\lambda(t)\). There is a representation of \(w(t)\) in generators with the residue \(-t\pmod m\). Conversely any such nonnegative combination of \(g_j\) (excluding \(m\) in an Apéry minimizer) corresponds to a coin total \(T=t+qm\) and \(h\) coins, with \(q\ge0\), and has value \(At+m(Aq+h)\). If \(q=0\), this is at least \(w(t)\); if \(q\ge1\), it is strictly larger because \(\lambda(t)\le t\le A\) and \(h\ge1\). Thus \(w(t)\) is the unique Apéry representative in residue \(-t\pmod m\). This argument applies to the full generating family. In particular, \(p(t)=w(t)-m\notin S_n\).

For each generator \(g_j\), if \(t+c_j\le A\), then \(p(t)+g_j-w(t+c_j)=m(\lambda(t)-\lambda(t+c_j))\), so membership follows whenever \(\lambda(t+c_j)\le\lambda(t)\). If \(t+c_j\ge m\), write \(t+c_j=t'+qm\), where \(0\le t'\le A\) and \(q\ge1\). Then \(p(t)+g_j-w(t')=m(Aq+\lambda(t)-\lambda(t'))\ge0\), because \(\lambda(t')\le A\). Thus wrapping additions always give membership. The generator \(m\) is automatic. Consequently it suffices for each candidate \(t\) to verify \(\lambda(t+c_j)\le\lambda(t)\) for every coin \(c_j\le A-t\).

**2. Coin-count bounds.** For every integer \(q\ge1\) and \(0\le u\le2^q-1\), one has \(\lambda(u)\le q\). Induct on \(q\): if \(u<2^{q-1}-1\) use induction; if \(2^{q-1}-1\le u\le2^q-2\), subtract one coin \(2^{q-1}-1\) and apply induction to the residual \(\le2^{q-1}-1\); if \(u=2^q-1\), use one coin. Also \(\lambda(B)\le2\), \(\lambda(B+1)\le3\), \(\lambda(B+2)\le2\), so \(\lambda(u)\le n\) for \(0\le u\le B+2\).

Any sum of \(h\) Mersenne coins satisfies \(t+h=\sum_{i=1}^h 2^{j_i}\), hence \(h\equiv t\pmod2\) and \(s_2(t+h)\le h\), where \(s_2\) is binary digit sum. We use this as a *necessary* condition, not as a sufficient characterization. For \(1\le d\le n\), splitting \(B\) into \(d\) powers of two of size at least two gives \(\lambda(B-d)\le d\). If \(h=d-2r<d\) were admissible, with \(r\ge1\), then \(s_2(B-2r)=n-1-s_2(r-1)>d-2r=h\), because \(d\le n\) and \(s_2(r-1)\le r-1\); contradiction. Therefore \(\lambda(B-d)=d\) for \(1\le d\le n\).

For \(5\le d\le n+2\), \(A-d=(4B-1)+(2B-1)+(B-(d-2))\) gives \(\lambda(A-d)\le d\). A purported shorter count \(h=d-2r\) would satisfy \(s_2(A-2r)=n+1-s_2(r-1)>d-2r\), since \(A-2r=6B+(B-2r)\), \(2r<B\), and \(d\le n+2\). Thus \(\lambda(A-d)=d\). Direct coin decompositions yield \(\lambda(A)=4\) (the three coins \(4B-1,2B-1,B-1\) plus coin \(3\)), and \(\lambda(A-1)=5\) (the same three large coins plus two ones). The lower bounds follow by testing the smaller admissible counts with binary digit sums: for \(A\), \(h=2\) fails since \(s_2(A+2)=4\); for \(A-1\), \(h=1,3\) fail since \(s_2(A)=3\) and \(s_2(A+2)=4\). Finally \(\lambda(A-2)\le4\), \(\lambda(A-3)\le3\), \(\lambda(A-4)\le4\), using respectively the three large coins plus one one, just the three large coins, and \((4B-1)+(2B-1)+2(B/2-1)\).

**3. Two separated suffix maxima.** Let \(t_1=4B-n-2\) and \(t_2=6B-n-2\). Represent them respectively as \((2B-1)+(B-1)+(B-n)\) and \((4B-1)+(B-1)+(B-n)\). The preceding equality \(\lambda(B-n)=n\) gives upper bounds \(n+2\). If \(h=n+2-2r<n+2\) were a representation count, then \(2r<B\), and in either case the integer \(t_i+h\) equals \(3B+(B-2r)\) or \(5B+(B-2r)\). Therefore \(s_2(t_i+h)=n+1-s_2(r-1)>n+2-2r=h\), a contradiction. Hence \(\lambda(t_1)=\lambda(t_2)=n+2\).

For every \(t\in[t_1,4B-2]\), subtract the coins \(2B-1\) and \(B-1\); the remainder lies between \(B-n\) and \(B\), so \(\lambda(t)\le n+2\). For \(4B-1\le t\le7B\), subtract \(4B-1\), leaving \(0\le u\le3B+1\). If \(u\le2B-2\), the first coin-count bound (and, where necessary, subtraction of \(B-1\)) gives \(\lambda(u)\le n+1\). If \(u\ge2B-1\), subtract \(2B-1\), leaving at most \(B+2\), so again \(\lambda(u)\le n+1\). Thus \(\lambda(t)\le n+2\) throughout \([t_1,A]\). Both \(t_1\) and \(t_2\) are therefore valid indices by Step 1.

**4. The remaining indices.** At \(t=A\), every positive coin causes wrap, so Step 1 applies. At \(t=A-1\), the only nonwrapping coin is \(1\), and \(\lambda(A)=4\le5=\lambda(A-1)\). Finally let \(t=A-d\) with \(5\le d\le n+2\). For each nonwrapping coin \(c_j\le d\), put \(e=d-c_j\). If \(e\ge5\), the exact formula yields \(\lambda(A-e)=e\le d\). For \(0\le e\le4\), the displayed finite upper bounds give \(\lambda(A-e)\le5\le d\). Thus each such \(p(t)\) is pseudo-Frobenius. The indices \(t_1,t_2,A,A-1,A-5,\ldots,A-(n+2)\) are distinct for all \(n\ge3\), and distinct Apéry residues ensure distinct pseudo-Frobenius values. There are \(n+2\) of them. \(\square\)

## Verification
The standalone standard-library script `verify.py` uses independent Dijkstra shortest paths on residues modulo \(A+1\) and a separate coin-change dynamic program for every \(3\le n\le9\). It checks the Apéry identity, the displayed candidate membership, exact special coin lengths, and exhaustive pseudo-Frobenius recognition in those finite instances. It returns `VERIFY_OK n_levels=7 candidate_instances=56`. The infinite assertion is established by the foregoing symbolic proof, not by finite tests.

## Relationship to prior work
Srivastava and Thakkar introduced Proth numerical semigroups and analyzed embedding dimensions and Frobenius numbers (2023, arXiv:2311.12462). Liu, Xin, Ye and Yin (2023, arXiv:2306.03459) treated greedy Apéry models and determined pseudo-Frobenius sets for several other positive-offset families, while also treating Proth-related Frobenius problems. Their proofs of Frobenius/genus formulas do not by themselves determine these explicit pseudo-Frobenius values for the \(7\)-family. Liu et al.'s later Semigroup Forum article (2025, DOI 10.1007/s00233-025-10518-1) addresses generalized Frobenius/genus formulas; the full updated article has not been completely inspected, so an unrecognized overlap remains a bibliographic risk.

## Limitations
Only \(n+2\) specified pseudo-Frobenius elements and the resulting lower bound are proved. No claim is made that these are all the pseudo-Frobenius numbers or that the lower bound is globally optimal. Source discovery is not a proof of priority, and the later full-text comparison is incomplete. No independent mathematical audit has been performed.

## References
- F. Liu, G. Xin, S. Ye, J. Yin, *A Combinatorial Model of Numerical Semigroup* (2023), arXiv:2306.03459, https://arxiv.org/abs/2306.03459 (first public 2023-06-06).
- P. Srivastava, D. Thakkar, *The Frobenius Problem for the Proth Numbers* (2023), arXiv:2311.12462, https://arxiv.org/abs/2311.12462 (first public 2023-11-21).
- F. Liu, G. Xin, S. Ye, J. Yin, *On the Frobenius number and genus of a collection of semigroups generalizing repunit numerical semigroups*, *Semigroup Forum* 110 (2025), DOI:10.1007/s00233-025-10518-1.
