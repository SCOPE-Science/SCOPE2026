# An infinite ternary-morphism family with nonregular binary abelian complexity

## Finding
For each integer \(r\ge4\), let \(k=r+1\). On \(\mathcal A=\{0,1,2\}\) define the uniform substitution
\[
\sigma_r(a)=\underbrace{aa\cdots a}_{r\text{ copies}}(a+1\bmod3),
\qquad s_r=\lim_{j\to\infty}\sigma_r^j(0).
\]
Let \(b_r(i)=1\) exactly when \(s_r(i)=0\), and \(b_r(i)=0\) otherwise. For each \(n\ge1\), denote by \(\rho_r(n)\) the number of different counts of \(1\) among all length-\(n\) factors of \(b_r\). **Theorem.** The binary word \(b_r\) is \(k\)-automatic, but \(\rho_r\) is not \(k\)-regular. The theorem holds for all \(r\ge4\), without a finite cutoff. An identical argument gives the known case \(r=3\), which is not claimed as new.

The exact quantitative identity used in the proof is
\[
\rho_r(k^0)=2,\qquad
\rho_r(k^{m+1})-\rho_r(k^m)
=r\left(\max_{a\in\mathcal A}N_m(a)-\min_{a\in\mathcal A}N_m(a)\right),
\quad N_m(a)=|\sigma_r^m(0)|_a,
\]
for every integer \(m\ge0\). The incidence recurrence is
\[
N_0=(1,0,0),\qquad
N_{m+1}(a)=rN_m(a)+N_m(a-1\bmod3).
\]

## Assumptions and scope
All words are one-sided infinite words indexed from \(0\). Factors are contiguous blocks and abelian equivalence for binary words is equality of their numbers of \(1\)'s. A sequence with integer values is \(k\)-regular if the \(\mathbb Z\)-module spanned by its \(k\)-kernel is finitely generated. The alphabet has exactly three letters, and the repetition count \(r\) is an arbitrary fixed integer at least four. All limits and inequalities are exact, not asymptotic approximations.

## Proof
**1. Automaticity and complete adjacent-pair set.** Reading the base-\(k\) digits of \(i\), each digit equal to \(r\) contributes \(1\) modulo \(3\) and every other digit contributes \(0\). Consequently
\[
s_r(i)\equiv\#\{\text{base-}k\text{ digits of }i\text{ equal to }r\}\pmod3.
\]
A three-state digit automaton, followed by the stated coding, proves \(k\)-automaticity. Every ordered pair of letters occurs in \(s_r\): all letters occur, the substitution creates \(aa\) and \(a(a+1)\), and the occurrence of \(aa\) also creates \((a+1)a\) at the boundary of \(\sigma_r(aa)\). These three forms, with \(a\) varying modulo \(3\), exhaust the nine ordered pairs.

**2. Weighted factor extremum lemma.** Let \(w:\mathcal A\to\mathbb R\) be any fixed letter weight, extend it additively to finite words, and set \(U_m(a)=\sigma_r^m(a)\), \(Q=k^m\), and \(W_m(a)=w(U_m(a))\). Denote by \(H_m\) the maximum weight among *all* length-\(Q\) factors of \(s_r\). We claim that for each \(m\ge0\),
\[
H_{m+1}=H_m+r\max_aW_m(a).\tag{1}
\]
For the upper bound, decompose a length-\(kQ\) factor into level-\(m\) blocks. If aligned, its weight is at most \(k\max W_m\le H_m+r\max W_m\). Otherwise it consists of a suffix of one level-\(m\) block, exactly \(r\) complete level-\(m\) blocks, and a prefix of another. Since every ordered pair of letters occurs, concatenating those two end blocks yields a legal length-\(Q\) factor of weight equal to the two partial pieces. Their total is at most \(H_m\), while the complete blocks weigh at most \(r\max W_m\).

For the matching lower bound we inductively maintain the following stronger property: for some letter \(c\) satisfying \(W_m(c)=\max_aW_m(a)\), a maximum-weight length-\(Q\) factor occurs within \(U_m(c-1)U_m(c)\) or \(U_m(c)U_m(c+1)\), with indices modulo three. It is immediate at \(m=0\). The incidence identity
\[
W_{m+1}(a)=rW_m(a)+W_m(a+1)
\]
and the inequality
\[
W_{m+1}(c)-W_{m+1}(c+1)
=(r-1)(W_m(c)-W_m(c+1))+(W_m(c)-W_m(c-1))\ge0
\]
show that a maximizing letter at level \(m+1\) may be chosen from \(\{c-1,c\}\). Furthermore,
\[
U_{m+1}(c-1)U_{m+1}(c)
=U_m(c-1)^rU_m(c)^{r+1}U_m(c+1).
\]
Inside this concatenation we may enlarge the assumed maximizing length-\(Q\) factor crossing either indicated pair by exactly \(r\) full copies of \(U_m(c)\): use the final copy of \(U_m(c-1)\) followed by \(r+1\) copies of \(U_m(c)\) in the first case, or the \(r+1\) copies of \(U_m(c)\) followed by \(U_m(c+1)\) in the second case. The resulting factor has length \(kQ\), weight \(H_m+rW_m(c)\), and crosses the level-\(m+1\) boundary of the displayed concatenation. This is one of the two required neighboring pairs for either choice \(c'\in\{c-1,c\}\). Thus the stronger property and equality in (1) follow by induction.

Apply (1) to weights \(w(a)=\mathbf1_{a=0}\) and \(w(a)=-\mathbf1_{a=0}\). If \(h_m\) and \(\ell_m\) are respectively the maximum and minimum counts of zeros in length-\(Q\) factors of \(s_r\), then
\[
h_{m+1}-h_m=r\max_aN_m(a),\qquad
\ell_{m+1}-\ell_m=r\min_aN_m(a).
\]
Since moving a binary window by one position changes its count by at most one, and all windows occur along the same infinite word, every integer between \(\ell_m\) and \(h_m\) occurs. Therefore \(\rho_r(k^m)=h_m-\ell_m+1\), proving the stated identity.

**3. Parity obstruction.** Put \(\omega=e^{2\pi i/3}\), \(z=r+\omega\), \(R=|z|=\sqrt{r^2-r+1}\), and \(\theta=\arg z\). The discrete Fourier transform of the incidence recurrence gives
\[
N_m(a)=\frac{k^m+2R^m\cos(m\theta-2\pi a/3)}3.\tag{2}
\]
In particular,
\[
\cos(2\theta)=\frac{2r^2-2r-1}{2r^2-2r+2}\in(1/2,1)
\qquad (r\ge3).\tag{3}
\]
If \(\theta/\pi\) were rational, \(2\cos(2\theta)\) would be both rational and an algebraic integer, hence an integer. Formula (3) puts it strictly between \(1\) and \(2\), a contradiction. Thus \(\theta/\pi\) is irrational, and (2) also ensures that the three entries of \(N_m\) are pairwise distinct for \(m>0\).

Reduce the incidence matrix \(rI+C\) modulo two, where \(C\) is the cyclic coordinate shift. If \(r\) is even, \(N_{3t}\equiv(1,0,0)\pmod2\); if \(r\) is odd, \(N_{3t}\equiv(0,1,1)\pmod2\), for each integer \(t\ge1\). The latter follows from \((I+C)^3=C+C^2\) and \((C+C^2)^2=C+C^2\) over \(\mathbb F_2\). Hence in both cases the first coordinate has parity opposite to the other two. Writing \(g_m=\max_aN_m(a)-\min_aN_m(a)\), it follows, for \(t\ge1\), that
\[
g_{3t}\equiv0\pmod2
\quad\Longleftrightarrow\quad
(N_{3t}(0)-N_{3t}(1))(N_{3t}(0)-N_{3t}(2))<0.
\]
An exact trigonometric identity derived from (2) yields
\[
(N_m(0)-N_m(1))(N_m(0)-N_m(2))
=\frac{R^{2m}}3(4\cos^2(m\theta)-1).
\]
Thus
\[
g_{3t}\equiv0\pmod2\quad\Longleftrightarrow\quad |\cos(3t\theta)|<\frac12.\tag{4}
\]
Because \(\theta/\pi\) is irrational, the right-hand truth value of (4) is not eventually periodic in \(t\). Indeed, on each progression \(t=t_0+pj\), the angles \(3(t_0+pj)\theta\bmod2\pi\) are dense and meet both the strict sublevel and strict superlevel sets infinitely often.

**4. Contradiction to regularity.** If the integer-valued sequence \(\rho_r\) were \(k\)-regular, its reduction modulo \(2r\) would be \(k\)-automatic: a finitely generated \(\mathbb Z\)-module of kernel sequences has finite image modulo any integer. Hence \(m\mapsto\rho_r(k^m)\bmod2r\), which is obtained by feeding the automaton the base-\(k\) representation consisting of one \(1\) and \(m\) zeros, would be eventually periodic. Its first differences modulo \(2r\) would also be eventually periodic. But by (1) these differences equal \(r g_m\bmod2r\), and their restriction to indices \(m=3t\) distinguishes exactly the non-eventually-periodic parities in (4). Contradiction. \(\square\)

## Verification
The fully finite scripts `proof_check.py` and `digit_verifier.py` are embedded with this result, along with `verification_output.txt`. The first exhaustively checks all factors of length \(k^m\) by scanning the nine two-block concatenations \(U_m(a)U_m(b)\), for \(2\le r\le7\) and the stated finite depths. Every factor of that length is present in one of these concatenations because all nine ordered pairs occur. The second checks separately generated base-\(k\) digit sequences for \(4\le r\le9\) and finite depths, together with the parity intermediate claim for \(t=1,\ldots,14\). Both reproduce the recurrence values wherever their parameter ranges overlap. These computations test the proof but do not replace its induction, algebraic irrationality, or infinite-density arguments.

## Relationship to prior work
Allouche, Rampersad, Rigo, Shallit, and Stipulanti [1] construct and prove the nonregularity of the individual \(r=3\) instance; they also discuss other repetition counts. The present theorem retains the ternary alphabet, handles *every* repetition count \(r\ge4\), and proves the parity obstruction uniformly, including the even-\(r\) cases via reduction modulo \(2r\). The weighted extremum induction is adapted from the source's technique rather than claimed as an independently new general method.

Rigo, Stipulanti, and Whiteland [2] establish regularity-related results for Parikh-collinear morphisms, which have incidence rank one. The incidence matrix here is \(rI+C\), which has full rank for \(r\ge4\), so those positive theorems do not cover these words. Popoli, Shallit, and Stipulanti [3] study additive complexity and automatic computation without establishing this full parametric nonregularity family.

## Limitations
The theorem concerns a fixed three-letter cyclic alphabet and repetition counts at least four. It does not classify all uniform morphisms, all alphabet sizes, or arbitrary codings. The case \(r=3\) belongs to the cited earlier work, and this theorem is not a claim of its priority. The literature comparison cannot exclude unindexed or otherwise undiscovered equivalent formulations; independent mathematical and priority review have not been performed.

## References
[1] J.-P. Allouche, N. Rampersad, M. Rigo, J. Shallit, M. Stipulanti, *An example of an automatic sequence with non-regular abelian complexity*, arXiv:2610.03837v1, first public 2026-10-02, https://arxiv.org/abs/2610.03837.

[2] M. Rigo, M. Stipulanti, M. Whiteland, *Automatic Abelian Complexities of Parikh-Collinear Fixed Points*, arXiv:2405.18032, https://arxiv.org/abs/2405.18032.

[3] P. Popoli, J. Shallit, M. Stipulanti, *Additive word complexity and Walnut*, arXiv:2410.02409, https://arxiv.org/abs/2410.02409.
