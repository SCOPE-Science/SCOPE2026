# Sharp fixed-content spectrum of cyclic binary two-binomial profiles

## Finding

Let \(p,q\) be positive integers, \(N=p+q\), \(d=\gcd(p,q)\), and \(L=N/d\). For a binary word \(w\) with \(p\) zeros and \(q\) ones, let \(C(w)\) count the distinct two-binomial profiles of its \(N\) indexed cyclic rotations. A two-binomial profile records the counts of all scattered subsequences of lengths one and two. Then
\[
\boxed{L\le C(w)\le N-d+1.}
\]
Every integer in this interval occurs with the same prescribed content \((p,q)\). Lower equality holds exactly when \(w=u^d\), with \(u\) containing \(p/d\) zeros and \(q/d\) ones. The word \(0^p1^q\) attains upper equality.

For distinct rotation starts \(i,j\), their profiles coincide if and only if the directed arc from \(i\) to \(j\), of length \(\ell\), has exactly \(\ell q/N\) ones. In particular \(N\mid \ell q\) is necessary for a collision.

## Assumptions and scope

The words are finite and on \(\{0,1\}\). An occurrence of a scattered pair \(ab\) is an ordered pair of strictly increasing positions carrying \(a,b\), not necessarily neighboring. Rotations are indexed by start even if the resulting strings agree; \(C(w)\) counts different profiles, not multiplicities. A directed arc includes its first start but excludes its second, and has length in \(\{1,\ldots,N-1\}\) when the starts are distinct.

For fixed content, the profile is determined by \(F(v)=\binom v{01}\): the same-letter pair counts are \(\binom p2\) and \(\binom q2\), and \(\binom v{10}=pq-F(v)\).

## Proof

**Height identity and collisions.** Write \(f_i=F(\rho_i(w))\), where \(\rho_i\) is the rotation starting at position \(i\) and positions start at zero. Moving a leading zero to the end removes \(q\) scattered `01` pairs; moving a leading one to the end adds \(p\). If \(B_i\) counts ones in the prefix of length \(i\), then
\[
f_i-f_0=NB_i-qi=:h_i,\qquad 0\le i\le N.
\]
Since \(h_N=h_0=0\), heights may be extended periodically. The height difference along an arc with \(b\) ones and length \(\ell\) is \(Nb-q\ell\), which proves the exact collision assertion. Replacing the choice of cyclic origin translates the heights and does not change their number.

**Lower bound and equality.** The congruence \(h_i\equiv-qi\pmod N\) implies that equal heights have start indices congruent modulo \(L\). Hence there are at least \(L\) heights. If there are exactly \(L\), each residue class has a single height, so \(h_{i+L}=h_i\) for every cyclic index \(i\). Differences of consecutive heights then give \(Nw_{i+L}-q=Nw_i-q\), so \(w=u^d\), with the indicated content of \(u\). Conversely, in \(u^d\) every length-\(L\) arc contains \(q/d\) ones, so heights repeat with period \(L\); the congruence still distinguishes the \(L\) residue classes.

**Upper bound by balanced-window deletion.** Suppose \(d\ge2\). For all \(N\) cyclic starts, count the ones in the window of length \(L\). Each one is counted \(L\) times, so the average window count is the integer \(q/d\). Successive counts differ by at most one. If not all are the average, there are counts on both sides of the average; some count is exactly the average since the counts change by at most one. The corresponding arc has zero height displacement.

Use **normalized** heights \(g_i=h_i/d=L B_i-(q/d)i\). These have the same equality classes as the original heights and increments \(p_0=p/d\) on ones and \(-q_0=-q/d\) on zeros. Choose the beginning of the balanced arc as origin, so that \(g_0=g_L=0\). Delete the first \(L\) letters. The remaining word \(v\) has content \(((d-1)p_0,(d-1)q_0)\) and gcd \(d-1\). Its normalized increments are precisely \(p_0,-q_0\), hence its normalized height at each of its \(N-L\) starts equals the old normalized height at the corresponding retained start \(L,\ldots,N-1\). This equality uses the normalization: the unnormalized increments for the shortened word are scaled by \((d-1)/d\). The deleted start 0 has the same height as retained start \(L\); the other deleted starts can contribute at most \(L-1\) distinct heights. Thus \(C(w)\le C(v)+L-1\). For \(d=1\), the number of indexed starts gives \(C(w)\le N=N-d+1\). Induction gives
\[
C(w)\le ((d-1)L-(d-1)+1)+(L-1)=N-d+1.
\]

**Upper witness.** For \(w=0^p1^q\), the heights are the two injective progressions \(-a q\), \(0\le a\le p\), and \(-pq+bp\), \(1\le b\le q-1\). The latter omits the final return to the initial height. An intersection requires \((p-a)q=bp\), or \(p-a=k(p/d),\ b=k(q/d)\) with \(1\le k\le d-1\). There are exactly \(d-1\) intersections and therefore \(N-d+1\) different heights.

**No gaps.** Swapping adjacent unequal letters in a linear word changes exactly one of the prefix counts \(B_i\) among the indexed starts. Replacing a single entry of the height multiset changes its number of distinct entries by at most one. Every word of the prescribed content can be converted to \(0^p1^q\) by adjacent unequal swaps. Starting at a word \(u^d\), the class count must therefore visit every integer between the two endpoint counts.

## Verification

The preceding arguments prove the claims for all positive contents. The unchanged reference program `checker.py` can be replayed with `python3 checker.py` alongside this document. For 32,738 mixed words of lengths 2 through 14 it constructs the indexed rotations and explicitly counts all four scattered pairs, cross-checks the resulting number of profiles against the height formula, checks height collisions against balanced arcs, and tests extremal bounds, lower equality recognition and complete fixed-content attainment. It also checks witnesses and balanced windows for 9,801 content pairs. These are finite diagnostics, not a proof of the unbounded theorem.

## Relationship to prior work

Binomial equivalence and its class structure are treated by Rigo and Salimov and by Lejeune, Rigo and Rosenfeld. The proof of Rigo and Salimov's Theorem 16 in their extended paper already uses the one-letter rotation update of the `01` statistic; the fixed-content rotation-count spectrum is not the conclusion of that infinite-word theorem. Richomme's partition description concerns words within a fixed profile class, not the number of profile classes visited by one rotation orbit.

Chuan's conjugate-moment set uses \(M(v)=\sum_{j=1}^N (N+1-j)v_j\). At fixed content \(M(v)=q(2N+1-q)/2-F(v)\), so the set of moments of conjugates is an affine image of the same set of profile values. The accessible abstract addresses moment spread and consecutiveness; the full text was not available for comparing fixed-content cardinality theorems. The encoding and the one-letter update are not claimed as new.

The separate multiletter result (Resultary `0d4f8c02fe70`) has a related balanced-arc criterion and adjacent-swap argument, but its full spectrum \([L,N]\) assumes at least three letters and does not prove the binary upper bound. A separate binary record (Resultary `4ff94afd6c61`) gives matching sharp endpoints and the power-word criterion but expressly leaves the intermediate values open. The result here gives the entire binary spectrum; no historical priority between records is asserted.

## Limitations

The theorem concerns the whole-word cyclic rotations of mixed binary words and binomial order two. It does not classify all upper extremizers, resolve higher binomial orders or resolve the historical priority question left by the unavailable Chuan full text.

## References

1. M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, extended version, p. 12, Theorem 16 and proof. https://orbi.uliege.be/bitstream/2268/178703/1/binomial_TCS_final.pdf
2. M. Lejeune, M. Rigo and M. Rosenfeld, *On the binomial equivalence classes of finite words*, 2020. https://orbi.uliege.be/bitstream/2268/249124/1/LejeuneRigoRosenfeld-ijacVersion2.pdf
3. G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159. https://arxiv.org/abs/2510.07159
4. W.-F. Chuan, *Moments of conjugacy classes of binary words*, Theoretical Computer Science, 2004. https://doi.org/10.1016/S0304-3975(03)00398-0
5. *Sharp 2-binomial rotation spectra for fixed multiletter content*. https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-sharp-2-binomial-rotation-spectra-for-fixed-multiletter-content--0d4f8c02fe70
6. *Sharp cyclic 2-binomial fingerprint bounds at fixed binary weight*. https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-sharp-cyclic-2-binomial-fingerprint-bounds-at-fixed-binary-weigh--4ff94afd6c61
