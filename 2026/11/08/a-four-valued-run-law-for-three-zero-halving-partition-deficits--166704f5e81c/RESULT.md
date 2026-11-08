# A four-valued run law for three-zero halving-partition deficits

## Finding
Let \(a(n)\) count the halving partitions of \(n\) defined below, and let \(s(n)\) be Stern's diatomic sequence. For every \(n\ge1\), let \(u\) be the odd part of \(n\). If the canonical binary expansion of \(u\) has exactly three zero digits, then
\[
 s(n)-a(n)=\rho(u-1),
\]
where \(\rho(v)\) counts the maximal nonempty blocks of consecutive ones in the ordinary binary expansion of \(v\). In particular, the deficit belongs to \(\{1,2,3,4\}\), and all four values occur.

## Assumptions and scope
A halving partition of a positive integer \(n\) is a finite sequence of positive integers \(p_1,\ldots,p_k\) such that \(\sum_{i=1}^{k}p_i=n\), \(p_1\in\{\lfloor n/2\rfloor,\lceil n/2\rceil\}\), and \(p_i\in\{\lfloor p_{i-1}/2\rfloor,\lceil p_{i-1}/2\rceil\}\) for all \(2\le i\le k\). Distinct sequences are counted separately. Set \(a(n)\) equal to their number. Stern's sequence is \(s(0)=0\), \(s(1)=1\), \(s(2m)=s(m)\), and \(s(2m+1)=s(m)+s(m+1)\) for \(m\ge1\). The assertion applies to every positive integer whose odd part has exactly three zero bits; leading zero digits do not count. No upper bound on \(n\) is imposed.

## Proof
**Step 1: reduce to odd arguments and encode chains.** The identities \(a(2m)=a(m)\) and \(s(2m)=s(m)\) reduce the claim to an odd integer \(u>1\). Put \(h=\lfloor\log_2u\rfloor\), \(N=u-1\), and \(w=s_2(N)\), where \(s_2\) is binary Hamming weight. Since \(u\) starts and ends with \(1\) and has precisely three zero digits, \(h\ge4\) and
\[w=h-3.\]

A *hyperbinary expansion* of \(N\) is a finite sequence \(e=(e_j)_{j\ge0}\) with \(e_j\in\{0,1,2\}\) and \(N=\sum_{j\ge0}e_j2^j\). Define its length \(W(e)=\sum_j e_j\). It is classical that the number of such expansions is \(s(N+1)=s(u)\). For an integer cut \(t\ge1\), define
\[
 L_t(e)=\sum_{j<t}e_j,\qquad R_t(e)=\sum_{j\ge t}e_j2^{j-t},\qquad F_e(t)=1+L_t(e)+R_t(e)-t.
\]
Call the cut *eligible* if \(e_j\le1\) at every \(j\ge t\). It is *admissible* when it is eligible and \(F_e(t)=0\).

The admissible-cut criterion is proved by the usual halving-digit balance, as follows. Given a halving partition, put \(p_0=u\) and choose the unique \(q_i\in\{0,1,2\}\) with \(p_{i-1}=2p_i+q_i-1\). Its sum condition is equivalent to
\[\sum_{i=1}^tq_i=t-p_t,\qquad u-1=(p_t-1)2^t+\sum_{i=1}^tq_i2^{i-1}.\]
Writing the lower \(t\) digits as \(q_i\) and the upper digits as the ordinary binary expansion of \(p_t-1\) gives an eligible cut and \(F_e(t)=0\). Conversely, at an admissible cut, set \(p_t=R_t+1\), \(q_i=e_{i-1}\), and reconstruct by \(p_{i-1}=2p_i+q_i-1\). The two displayed identities guarantee \(p_0=u\) and \(\sum p_i=u\). All parts are positive because \(p_t\ge1\) and each backward step preserves positivity; consecutive parts satisfy the required halving choices. The reconstruction is unique because
\[F_e(t+1)-F_e(t)=-R_{t+1}(e)-1<0.\]
Hence \(a(u)\) is exactly the number of hyperbinary expansions with an admissible cut. The deficit \(s(u)-a(u)\) counts those without any admissible cut. This correspondence agrees with Lemma 11 and Theorem 12 of Alekseyev [1].

**Step 2: classify expansion lengths.** Repeatedly replacing two copies of \(2^j\) by one copy of \(2^{j+1}\) converts any hyperbinary expansion to the unique ordinary binary expansion, decreasing \(W\) by exactly one at each carry. Consequently \(W\ge w=h-3\).

If \(W\ge h-1=w+2\), take \(t=W+1\ge h\). Because \(N<2^{h+1}\), the only possibly nonzero digit at index at least \(h\) is a single \(1\) at index \(h\). Thus the upper tail at that cut is ordinary binary and \(L_t+R_t=W\). Therefore \(F_e(t)=1+W-t=0\); this expansion is admissible.

If \(W=w\), the expansion must be the ordinary binary one. Since \(e_h=1\), and the total weight is \(w=h-3\), at \(t=h-1\) one has
\[L_{h-1}=w-1-e_{h-1},\quad R_{h-1}=e_{h-1}+2,\quad F_e(h-1)=w-h+3=0.\]
This cut is eligible, so the ordinary expansion is admissible.

It remains to consider \(W=w+1=h-2\). Exactly one carry is needed to obtain the ordinary binary expansion. Thus this hyperbinary expansion is uniquely obtained by *splitting* one ordinary binary \(1\)-digit at position \(j\ge1\) into two digits at position \(j-1\). Such a split is permitted precisely when the ordinary bit at \(j-1\) is zero; otherwise the resulting digit would exceed \(2\). These splits are in bijection with the starts of maximal one-runs of \(N\), since \(N\) is even and ends in zero.

All these single-split expansions are inadmissible. If the split is below the leading bit (\(j<h\)), then \(e_h=1\). Because \(W=h-2\), one finds \(F_e(h)=-1\) and \(F_e(h-1)=1\); strict decrease excludes a zero at every integral cut. If the leading bit itself is split (\(j=h\)), then \(e_h=0\), \(e_{h-1}=2\), \(F_e(h)=-1\), and \(F_e(h-1)=0\), but the sole zero occurs at an *ineligible* cut, due to \(e_{h-1}=2\). Again there is no admissible cut. These are the only inadmissible expansions; their number is \(\rho(N)\). This proves \(s(u)-a(u)=\rho(u-1)\).

**Step 3: sharp range.** The three zeros of \(u\) create at most three interruptions of runs and, after its trailing \(1\) is changed to \(0\), \(u-1\) has between one and four one-runs. All occur: respectively \(u=17,35,75,171\), giving deficits \(1,2,3,4\). Multiplication by powers of two preserves both counts, completing the proof for all \(n\).

## Verification
Run the included standalone program with `python3 verify.py`. Its exact-integer checks independently compare the stated closed form against the generalized halving recurrence for all \(1{,}365\) eligible odd inputs below \(2^{16}\), directly enumerate halving partitions for \(384\) small inputs, and explicitly enumerate hyperbinary expansions and admissible cuts for \(35\) cases. See VERIFICATION.md for the observed output and limitations. No finite computation is used as a substitute for the preceding proof.

## Relationship to prior work
Alekseyev [1, Lemma 11, Theorem 12, Corollaries 13 and 18, Section 6] gives the admissible-cut interpretation and evaluates the deficit when the odd part has at most two zero digits; Section 6 explicitly asks for a direct formula when there are more. Its general coefficient formula provides an algorithm for computing any particular deficit, but it does not state or derive this uniform run-count law for exactly three zeros. The present proof supplies the new one-carry classification of all missing expansions. Dilcher and Ericksen [2] develop hyperbinary expansions and Stern polynomials, but not the halving-partition deficit. OEIS A349552 [3] tabulates \(a(n)\) and describes the original halving-count problem but does not state the infinite three-zero formula. McConville, Propp, and Sagan [4] study the hyperbinary-partition poset, not the halving-partition cut deficit.

## Limitations
The formula is restricted to exactly three zero digits in the *odd part*; it does not give the deficit for four or more zeros. The larger-zero question remains open in this work. General hyperbinary coefficient formulas can still evaluate individual examples. Exact finite checks are supplementary to the proof, not independent certification or a proof of historical priority. Earlier unindexed literature might contain an equivalent run-count formula.

## References
[1] M. A. Alekseyev, *Halving Partitions and Hyperbinary Expansions*, arXiv:2611.01243, publicly posted 2026-10-31. https://arxiv.org/abs/2611.01243 .

[2] K. Dilcher and L. Ericksen, *Hyperbinary Expansions and Stern Polynomials*, Electronic Journal of Combinatorics 22(2) (2015), P2.24. https://doi.org/10.37236/4822 .

[3] O. E. I. S., Sequence A349552, *Number of halving partitions of n*. https://oeis.org/A349552 .

[4] T. McConville, J. Propp, and B. E. Sagan, *Hyperbinary Partitions and q-Deformed Rationals*, arXiv:2508.20026 (2025). https://arxiv.org/abs/2508.20026 .
