# Positive factor frequencies and polylogarithmic discrepancy in Brik's word

## Finding
Let \(B_1=101\), and for each integer \(i\ge1\) obtain \(B_{i+1}\) by adjoining to \(B_i\) its suffix after the first \(i\) symbols. Let \(b\) be the resulting infinite word. For a nonempty binary word \(v\), let \(F_v(N)\) count occurrences of \(v\) wholly contained in the first \(N\) symbols of \(b\), with overlaps included. Then a limit
\[
\mu(v)=\lim_{N\to\infty}\frac{F_v(N)}{N}
\]
exists for **every** \(v\), and the quantitative estimate
\[
F_v(N)=\mu(v)N+O_{|v|}\bigl((1+\log_2(N+1))^2\bigr)
\]
holds uniformly for all integers \(N\ge1\). Moreover,
\[
\boxed{\mu(v)>0\ \Longleftrightarrow\ v\text{ contains no adjacent pair }00.}
\]
Consequently the cylinder frequencies define a shift-invariant Borel probability measure with full support on the golden-mean subshift (the set of infinite binary words avoiding `00`). The word \(b\) is a generic point of that measure. No assertion of ergodicity, mixing, or optimality of the discrepancy exponent is made.

## Assumptions and scope
Positions are one-based. The suffix appended at stage \(i\) is \(S_i=B_i[i+1..L_i]\), where \(L_i=|B_i|=2^{i-1}+i+1\); thus \(B_{i+1}=B_iS_i\) and \(L_{i+1}=2L_i-i\). An occurrence of \(v\) counts only when all its \(k=|v|\) positions lie in the specified finite prefix. Write \(C_i=F_v(L_i)\). The empty word is used only in the measure convention \(\mu(\varepsilon)=1\). The source work establishes recurrence of \(b\) and characterizes its factor language as exactly the binary words avoiding `00` [1, Theorems 3 and 7]; the arguments below also use the explicit recursion and independently check the necessary quantitative estimates.

## Proof
**1. A finite-block recurrence and rapidly convergent formula.** Let \(e_i(v)\) be the number of occurrences of \(v\) in \(B_i\) whose starting positions are at most \(i\). Let \(c_i(v)\) be the number of occurrences in \(B_{i+1}=B_iS_i\) that meet both sides of the junction between these blocks. Then \(0\le e_i(v)\le i\) and \(0\le c_i(v)\le k-1\). Every occurrence internal to \(S_i\) is exactly an occurrence in \(B_i\) starting beyond position \(i\). Hence
\[
C_{i+1}=2C_i-e_i(v)+c_i(v).\tag{1}
\]
Writing \(d_i=c_i(v)-e_i(v)\), we have \(|d_i|\le i+k-1\). Equation (1) gives the absolutely convergent, effective series
\[
\theta_v=C_1+\sum_{i=1}^{\infty}\frac{d_i}{2^i}
=\lim_{i\to\infty}\frac{C_i}{2^{i-1}},\qquad
\left|\theta_v-\frac{C_i}{2^{i-1}}\right|\le\frac{i+k}{2^{i-1}}.\tag{2}
\]
Since \(0\le C_i\le L_i\) and \(L_i/2^{i-1}\to1\), one has \(0\le\theta_v\le1\). Equation (2), together with \(L_i=2^{i-1}+i+1\), implies
\[
|C_i-\theta_v L_i|\le 2i+k+1.\tag{3}
\]

**2. Every-prefix discrepancy.** Fix \(N\ge L_1\), choose the unique \(i\) with \(L_i\le N<L_{i+1}\), and put \(t=N-L_i\), so \(0\le t<L_i-i\). The second part of the length-\(N\) prefix is \(B_i[i+1..i+t]\). Comparing occurrences ending in that part with occurrences in the length-\(i+t\) prefix of \(b\) gives
\[
F_v(N)=C_i+F_v(i+t)-F_v(i)+\eta_{i,t},\qquad |\eta_{i,t}|\le k-1.\tag{4}
\]
Indeed, at most \(k-1\) occurrences cross the removal boundary after position \(i\), and at most \(k-1\) cross the concatenation boundary after position \(L_i\); the correction is the difference of these two counts, each in \([0,k-1]\).

Set \(E_v(N)=F_v(N)-\theta_v N\). As \(0\le\theta_v\le1\), one has \(|E_v(i)|\le i\). Equations (3) and (4) imply
\[
|E_v(N)|\le|E_v(i+t)|+3i+2k.\tag{5}
\]
Because \(L_i\ge2i\) for \(i\ge1\), and the ratio \((i+t)/(L_i+t)\) is increasing in \(t\),
\[
\frac{i+t}{N}\le\frac{L_i}{2L_i-i}\le\frac23.\tag{6}
\]
Also \(i\le 1+\log_2 N\). Iterating (5) through arguments shrinking by a factor at most \(2/3\) reaches \(N<L_1\) after \(O(\log N)\) steps. The sum of the additive terms is \(O_k((1+\log_2(N+1))^2)\). This proves the claimed estimate and shows \(\mu(v)=\theta_v\) for every \(v\).

**3. Positivity for each permitted factor.** From [1, Theorems 3 and 7], every word \(v\) avoiding `00` occurs at arbitrarily large starting positions \(r\) of \(b\). Fix such an occurrence and let \(t\) be the smallest index satisfying \(L_t\ge r+k-1\). Since \(L_t\) grows exponentially, \(t=O_k(\log(r+1))\). For large \(r\), we have \(t<r\). Initially \(B_t\) contains the selected occurrence starting at \(r\). For every stage \(j\) with \(t\le j<r\), each designated occurrence in \(B_j\) starts at least at \(r>j\), hence survives in the appended suffix \(S_j\) and has a distinct copy there. Both copies still start at least at \(r\). It follows inductively that
\[
C_r\ge2^{r-t}.
\]
Applying the one-sided lower bound from (1) from stage \(r\) onward yields
\[
\mu(v)\ge\frac{C_r}{2^{r-1}}-\sum_{j=r}^\infty\frac{j}{2^j}
\ge\frac{2^{r-t}-(r+1)}{2^{r-1}}>0
\]
for sufficiently large \(r\), since \(t=O_k(\log r)\). Conversely, `00` never occurs in \(b\) [1, Theorem 7], so any \(v\) containing `00` has \(F_v(N)=\mu(v)=0\).

**4. Shift-invariant measure.** For every finite \(v\), the sum of the occurrence counts of \(v0\) and \(v1\) differs from \(F_v(N)\) by at most one; similarly, the sum of the counts of \(0v\) and \(1v\) differs by at most one. Dividing by \(N\) gives both consistency identities
\[
\mu(v)=\mu(v0)+\mu(v1)=\mu(0v)+\mu(1v).
\]
With \(\mu(\varepsilon)=1\), the cylinder values define a shift-invariant Borel probability measure on one-sided binary sequences. The positivity/zero characterization in step 3 shows that its support is exactly the golden-mean subshift. By the definition of \(\mu(v)\), \(b\) is generic for this measure.

## Verification
The standalone `check_brik.py` recomputes the defining words and independently checks the exact two-block recurrence (1) for all 30 binary patterns of lengths one through four across 16 transitions. It also checks the intermediate-prefix identity (4) for each integer prefix length up to \(65554\), and reproduces illustrative block counts for several factors, including `1111`. The recorded output appears in `checker_output.txt`. The checker tests finite consequences only; positivity for arbitrarily rare factors, existence for every finite factor, and the infinite quantitative estimate are established by the proof above.

Equation (2) gives a deterministic enclosure for each frequency using only finite words: its stage-\(i\) rational approximation has absolute error at most \((i+k)/2^{i-1}\). This is not a claim of an independently certified decimal expansion.

## Relationship to prior work
Shallit [1] introduced and analyzed this recursion, proving the precise factor language, recurrence, and existence (with transcendence) of the **single-letter** frequency of `1`. Those results supply the language and recurrence premises, but do not state a limiting frequency for every factor, positivity of all admissible cylinder probabilities, or a uniform polylogarithmic factor-count discrepancy. The crossing-boundary recurrence, positivity amplification, and all-pattern discrepancy estimate are the contribution asserted here. General facts about recurrent words or shift-invariant measures alone do not imply the positive existence of every individual factor frequency for this specific nonuniformly recurrent word. The measure is not asserted to be uniquely ergodic on the full golden-mean shift.

## Limitations
The bound is an upper bound and is not claimed to have sharp order. The implicit discrepancy constant depends on the factor length. The measure constructed is generic and fully supported, but ergodicity, mixing, entropy, and exact closed forms for arbitrary cylinder frequencies are not determined. Formula (2) is computable to any prescribed accuracy but may be computationally impractical for very long, initially rare factors. Independent validation has not been performed.

## References
[1] Jeffrey Shallit, *Brik's sequence: a strange recursion*, arXiv:2605.07542v1, first made public 2026-05-08. https://arxiv.org/abs/2605.07542 ; full proof particularly Proposition 1, Theorems 3, 7, 10.

[2] J. Berstel, A. Lauve, C. Reutenauer, F. V. Saliola, *Combinatorics on Words*, American Mathematical Society, 2009 (background terminology for factors and recurrence; no result of this source is used to assert the new quantitative claim).
