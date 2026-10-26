# Sharp first and second triple-sphere intersections for fixed-weight binary reconstruction

## Finding

Let \(n\ge4t\) and \(t\ge2\) be integers. For binary \(n\)-words put \(S_t(x)=\{z:d_H(z,x)=t\}\), and for three *distinct* centers define \(I_t(a,b,c)=|S_t(a)\cap S_t(b)\cap S_t(c)|\). The two largest distinct attainable intersection sizes are exactly
\[
M_1=\binom{n-2}{t-1},\qquad M_2=4\binom{n-4}{t-2},\qquad M_2<M_1.
\]
The first equality \(I_t(a,b,c)=M_1\) holds **if and only if** all three pairwise distances equal \(2\). Among every other triple, \(I_t(a,b,c)\le M_2\), and equality holds **if and only if** its three pairwise distances are \(2,2,4\) in some order. Consequently, in the binary fixed-weight-\(t\) substitution model with arbitrarily chosen *distinct* observations, the least number of observations guaranteeing a candidate-source list of size at most two is
\[
N_{\mathrm{list}\,2}=\binom{n-2}{t-1}+1\quad(n\ge4t,\ t\ge2).
\]
This is a worst-case combinatorial statement; it does not assert that a particular efficient decoder attains the threshold.

## Assumptions and scope

The alphabet is \(\mathbb F_2\), the channel alters exactly \(t\) coordinates on each use, and observed output sequences are pairwise distinct. The transmitted source can be any of the \(2^n\) words; there is no additional codebook or prior distribution. The theorem is claimed for all integer \(t\ge2\) and \(n\ge4t\), including the boundary \(n=4t\). No optimality of the blocklength condition is claimed.

A triple of distinct centers has no common exact-radius output if one pairwise distance is odd: for binary words, the parity of \(d_H(z,a)+d_H(z,b)\) equals that of \(d_H(a,b)\). Thus nonzero intersections have even pairwise distances.

## Proof

**1. Pair-intersection monotonicity.** For two centers at Hamming distance \(2d\), any common exact-radius-\(t\) output has precisely \(d\) changed coordinates in their symmetric-difference support. Hence
\[
F_d=|S_t(a)\cap S_t(b)|=\binom{2d}{d}\binom{n-2d}{t-d}\quad(0\le d\le t),
\]
and the intersection is empty if \(d>t\). For \(1\le d<t\),
\[
\frac{F_{d+1}}{F_d}=\frac{2(2d+1)}{d+1}\frac{t-d}{n-2d}\frac{n-t-d}{n-2d-1}<4\frac{t}{n}\le1.
\]
Here \((t-d)/(n-2d)\le t/n\) since \(n\ge2t\), the last fraction is at most one since \(d\le t-1\), and the first fraction is strictly below four. So \(F_d\) decreases strictly with \(d\ge1\). For \(t\ge3\), a triple with a pair at distance at least six has intersection at most
\[
F_3=20\binom{n-6}{t-3}<4\binom{n-4}{t-2}=M_2.
\]
Indeed the ratio is \(5(t-2)(n-t-2)/((n-4)(n-5))<1\): its denominator minus numerator equals \(t^2+4t>0\) at \(n=4t\) and increases with \(n\). For \(t=2\), any pair at distance at least six has empty intersection. It remains to analyze triples with every pair at distance at most four and at least one pair at distance four.

**2. A pair separated by four.** Translate one center to \(0\) and write the second as the characteristic vector of a four-element set \(A\). Any output common to their radius-\(t\) spheres chooses exactly two of these four coordinates and exactly \(s=t-2\) coordinates outside \(A\). Put \(v=n-4\); there are \(\binom vs\) possible outside subsets \(W\), each admitting six inside subsets \(Q\subseteq A\) of size two.

Let \(B\) be the support of the third center, distinct from the first two. Set \(j=|B\cap A|\) and \(U=B\setminus A\). Necessarily \(|B|\) is even. For each fixed \(W\), the remaining condition \(d_H(1_{Q\cup W},1_B)=t\) is
\[
|Q\cap(B\cap A)|+|W\cap U|=|B|/2.
\]
If \(j=1\) or \(3\), each specified overlap with \(B\cap A\) occurs for at most three of the six choices of \(Q\). If \(j=2\), each specified overlap occurs for at most four choices; four occurs only when \(|Q\cap(B\cap A)|=1\). Therefore these cases give at most \(3\binom vs\) or \(4\binom vs\), respectively.

If \(j=0\) or \(4\), \(U\ne\varnothing\) (because the third center is distinct), and evenness of \(|B|\) forces \(|U|=2h\) with \(h\ge1\). The intersection condition is equivalent to \(|W\cap U|=h\), and hence at most
\[
6\binom vs p_h,\qquad p_h=\frac{\binom{2h}{h}\binom{v-2h}{s-h}}{\binom vs}.
\]
If \(h>s\) this is zero. Otherwise \(v\ge4s+4\) yields \(p_{h+1}/p_h<4s/v<1\) for \(1\le h<s\), by the same ratio calculation as above. Thus \(p_h\le p_1=2s(v-s)/(v(v-1))<1/2\); for \(s=0\), all probabilities vanish. Therefore this case contributes fewer than \(3\binom vs\). We conclude every such triple has intersection at most \(M_2=4\binom vs\).

Equality in the preceding bound forces \(j=2\) and \(U=\varnothing\). To see the second necessity, if \(U\ne\varnothing\) then \(|U|=2h\), and either \(h>s\), so no \(W\) works, or \(h\le s\), in which case \(v-2h\ge s\) and some \(W\) is disjoint from \(U\), so its six inner choices cannot contribute four valid outputs. If \(j=2\) and \(U=\varnothing\), exactly four choices of \(Q\) work for each \(W\). The third center has weight two, and the pairwise distances are \(4,2,2\). Conversely each such distance configuration attains \(M_2\).

**3. All pairwise distances two.** A translation and permutation of coordinates take an equilateral triple to the supports \(\varnothing,\{1,2\},\{1,3\}\). A common output either includes coordinate \(1\) and excludes \(2,3\), or excludes \(1\) and includes \(2,3\). Accordingly its count equals
\[
\binom{n-3}{t-1}+\binom{n-3}{t-2}=\binom{n-2}{t-1}=M_1.
\]
Any triple not in this equilateral class either has an odd pairwise distance (zero intersection), a pairwise distance at least six (strictly below \(M_2\)), or a pair at distance four (at most \(M_2\), with equality classified above). The two numerical levels are separated strictly: 
\[
\frac{M_2}{M_1}=\frac{4(t-1)(n-t-1)}{(n-2)(n-3)}<\frac45,
\]
because \((n-2)(n-3)-5(t-1)(n-t-1)\) equals \(t^2+1>0\) at \(n=4t\) and increases thereafter.

**4. List-size threshold.** A set of \(N\) distinct channel outputs is compatible with three sources exactly when those outputs all lie in the intersection of three exact-radius spheres. The maximal such intersection contains \(M_1\) words; hence any \(N\ge M_1+1\) observations yield at most two candidates. Conversely, choose an equilateral triple of centers and any \(N\le M_1\) different common outputs: all three centers remain possible. Thus the claimed threshold is necessary and sufficient.

## Verification

The included standard-library script `verify_triple_spheres.py` computes the count independently from the four binary coordinate types \((10,01,11,00)\). For type multiplicities \((a,b,c,d)\), it uses exact integer arithmetic to evaluate
\[
\sum_{h=0}^c\binom ch\binom a{(a+c)/2-h}\binom b{(b+c)/2-h}\binom d{t-(a+c)/2-(b+c)/2+h},
\]
interpreting nonintegral binomial lower arguments as disallowed. It checks every type profile for \(t=2,3,4,5\) and \(4t\le n\le4t+4\), then uses separate direct binary-word enumeration on 15 designated triples. All 20 complete parameter grids and 23,340 profiles satisfy the two-level classification and its equality cases. The execution trace in `verification_output.txt` ends `TRIPLE_SPHERE_VERIFY_OK`. These finite checks are not the proof of the unlimited theorem.

## Relationship to prior work

Papadopoulou, Yehezkeally, Rameshwar and Wachter-Zeh (arXiv:2610.30001v1, public on 2026-10-21) formulate the exact-weight binary substitution reconstruction model and prove its worst-case **unique** reconstruction threshold \(2\binom{n-2}{t-1}+1\). Their treatment does not state the three-center maximum, runner-up value, or list-size-two consequence proved here. Yaakobi and Bruck's associative-memory theorem, Junnila–Laihonen–Lehtilä's list reconstruction results, and Junnila–Laihonen–Lehtilä–Padavu Devaraj's intersection formulas treat Hamming **balls** (up-to-\(t\) errors). Their general ball-intersection formula does allow arbitrary fixed-radius sphere-intersection counts by inclusion–exclusion; no novelty is claimed for the mere ability to compute a given triple. The present theorem instead optimizes *simultaneously over all distinct triples* for exact-radius shells, classifies **both** top levels and their rigid extremizers, and yields the sharp unencoded list-two threshold in the indicated sparse-error regime.

## Limitations

The length hypothesis \(n\ge4t\) is sufficient, not proved optimal. The theorem is binary and exact-radius, not a theorem for all alphabets or for up-to-\(t\) balls. It gives the worst-case number of *distinct* observations, not a decoding algorithm or a stochastic sample complexity. Equivalent extremal consequences hidden in earlier general intersection formulas cannot be categorically excluded by literature searching, and independent verification of mathematical priority has not been performed.

## References

- Vivian Papadopoulou, Yonatan Yehezkeally, V. Arvind Rameshwar, and Antonia Wachter-Zeh, *When Majority-Vote Fails: Sequence Reconstruction under Fixed-Weight Substitutions*, arXiv:2610.30001v1 (2026), https://arxiv.org/abs/2610.30001.
- Ville Junnila, Tero Laihonen, Tuomo Lehtilä, and Pavan Padavu Devaraj, *The Size of the Intersection of q-ary Hamming Balls*, arXiv:2606.09158 (2026), https://arxiv.org/abs/2606.09158.
- Ville Junnila, Tero Laihonen, and Tuomo Lehtilä, *The Levenshtein's Sequence Reconstruction Problem and the Length of the List*, arXiv:2211.08812 (2022), https://arxiv.org/abs/2211.08812.
- Eitan Yaakobi and Jehoshua Bruck, *On the Uncertainty of Information Retrieval in Associative Memories*, IEEE Transactions on Information Theory 65 (2019), 2155–2165, https://doi.org/10.1109/TIT.2018.2878750.
- Binh Vu, Shuche Wang, and Van Khu Vu, *List Reconstruction Problem with List Size Two*, arXiv:2605.23638 (2026), https://arxiv.org/abs/2605.23638.
