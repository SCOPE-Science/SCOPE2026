# Complete constant-run spectra and exact frequencies for all-one block-parity words

## Finding

For every integer \(k\ge2\), let \(s_k(n)\in\{0,1\}\) be the parity of the number of possibly overlapping appearances of the binary pattern \(1^k\) in the usual binary expansion of \(n\ge0\). A *maximal constant run* is a maximal nonempty consecutive interval of indices on which \(s_k\) is constant; the run at the left endpoint \(0\) is included. Set \(H=2^k\). Then the complete set of lengths of maximal constant runs, counting either symbol, is

\[
\mathcal R_k=\{1\}\cup\{2^j:1\le j\le k\}\cup\{H-2^j:0\le j\le k-2\}\cup\{H/2+1\}.
\]

Every displayed length occurs infinitely often, and no other length occurs. In particular, the maximum run length is exactly \(H\).

More precisely, define the limiting run count per \(H\) input positions, for positive integers \(\ell\), by

\[
\lambda_k(\ell)=\lim_{B\to\infty}\frac{1}{B}\#\{\text{maximal constant runs of length }\ell\text{ starting in }[0,BH)\}.
\]

All these limits exist. Write \(p=2/H\), \(\rho=(2-p)/3\), and initially set \(\lambda_k(\ell)=0\) for every \(\ell\). Assign the following contributions, **adding them where two displayed lengths coincide**:

\[
\begin{aligned}
\lambda_k(1)&\mathrel{+}=\tfrac12+\rho,\\
\lambda_k(2^j)&\mathrel{+}=2^{-j-1}&& (1\le j\le k-2),\\
\lambda_k(H-2^j)&\mathrel{+}=2^{-j-1}&& (1\le j\le k-1),\\
\lambda_k(H/2+1)&\mathrel{+}=H^{-1},\\
\lambda_k(H-1)&\mathrel{+}=(1+p)/6,\\
\lambda_k(H)&\mathrel{+}=(2-p)/6.
\end{aligned}
\]

Here \(\mathrel{+}=\) means to add the indicated contribution to the initial zero, not a programming operation. The conventions correctly handle \(k=2\), when \(H-1=H/2+1=3\). The total number of runs per \(H\) input positions is \(\Lambda_k=4(2-p)/3\). Thus the asymptotic run-start density among input positions is

\[
\delta_k=\frac{\Lambda_k}{H}=\frac{8(H-1)}{3H^2},
\]

and the limiting proportion of runs having length \(\ell\) is \(\pi_k(\ell)=\lambda_k(\ell)/\Lambda_k\). All nonzero frequencies are positive rational numbers, and \(\sum_{\ell}\ell\lambda_k(\ell)=H\).

The upper inclusion also settles the exclusion component of Hendel's Conjecture 8 for \(k\ge3\). In conjunction with the occurrence constructions in Hendel's Theorem 7, the conjectured list of *zero*-run lengths is exact. This last statement credits those earlier constructions; the present result independently classifies all constant-run lengths and their densities.

## Assumptions and scope

The binary expansion of \(0\) is the one-digit word \(0\). Counts of overlapping occurrences are reduced modulo \(2\), not taken as integer counts. All runs are in the one-sided infinite word indexed by \(\mathbb N_0\). The results hold simultaneously for all integers \(k\ge2\), without assumptions on how \(k\) grows with the observation interval. Frequencies count runs by their *starting positions*, and a run crossing the far endpoint is included when its start is before that endpoint; this choice affects finite counts by at most one compared with counting only completed runs.

## Proof

**1. Exact carry criterion.** Fix \(n\ge0\), and put \(t=\nu_2(n+1)\). Write the binary expansion of \(n\), permitting leading zero padding, as \(M\,0\,1^t\). Then \(n+1\) has expansion \(M\,1\,0^t\). The old suffix contributes exactly \((t-k+1)_+=\max(t-k+1,0)\) appearances of \(1^k\), and the new digit contributes exactly one new appearance precisely when the trailing-one count of \(M\) is at least \(k-1\). Because the trailing-one count of the integer \(M\) equals \(\nu_2(M+1)\), we have the exact identity

\[
s_k(n)\oplus s_k(n+1)\equiv (t-k+1)_+ +\mathbf1_{\{\nu_2(M+1)\ge k-1\}}\pmod2.
\tag{1}
\]

The argument includes \(M=0\), with trailing-one count zero. Thus the transition positions in the infinite word are completely determined by the binary carry of \(n+1\).

**2. Exact transitions in each dyadic block.** Fix a block index \(j\ge0\) and examine the \(H\) prospective transition positions \(jH\le n<(j+1)H\). Let \(s=\nu_2(j+1)\), \(q=(j+1)/2^s\) (which is odd), and \(m=\min(s,k-1)\). For each \(t\in\{0,\ldots,k-1\}\), the unique candidate with \(\nu_2(n+1)=t\) is

\[
n_t=(j+1)H-2^t-1.
\]

For this candidate the integer \(M\) in (1) is \((j+1)2^{k-t-1}-1\), so \(\nu_2(M+1)=s+k-t-1\); consequently it is a transition exactly when \(t\le s\). Hence the interior transitions in increasing order are \(n_m,n_{m-1},\ldots,n_0\). The only remaining candidate is \(n=(j+1)H-1\), with \(t=k+s\). Its prefix integer has trailing-one count \(\nu_2(q+1)-1\); (1) shows that it is a transition if and only if

\[
c_j\equiv s+1+\mathbf1_{\{q\equiv-1\pmod H\}}\pmod2
\quad\text{equals }1.
\tag{2}
\]

This completely describes the transition set, for every \(j\) and \(k\), with no infinite-state or experimental premise.

**3. Exhaustive gap classification.** Runs between successive transitions have length equal to the difference of their transition indices. Adjacent interior transitions \(n_t,n_{t-1}\) have difference \(2^{t-1}\), for \(1\le t\le m\). When the last transition of the block exists, it follows \(n_0\) by one step. Otherwise \(n_0\) is the final transition in the block.

For a cross-block gap, let \(v=\nu_2(j+2)\) and \(h=\min(v,k-1)\). The first transition in the next block occurs at \((j+2)H-2^h-1\), so the cross-block gap is

\[
H-2^h\quad\text{if }c_j=1,\qquad
H-2^h+1\quad\text{if }c_j=0.
\tag{3}
\]

For \(v=0\), both values of \(c_j\) are possible and (3) gives \(H-1\) and \(H\). For \(1\le v<k\), \(j+1\) is odd, \(s=0\), and \(j+1\not\equiv-1\pmod H\); therefore \(c_j=1\) and the gap is \(H-2^v\). For \(v\ge k\), again \(s=0\), but now \(j+1\equiv-1\pmod H\); therefore \(c_j=0\), giving gap \(H/2+1\). The interior and cross-block lists together yield exactly \(\mathcal R_k\), with no further possibilities, apart from the initial prefix before the very first transition. That prefix has length \(H-1\), already in the list.

**4. Exact natural frequencies and occurrence.** Over nonnegative block indices \(j\), the natural density of \(\nu_2(j+1)=t\) is \(2^{-(t+1)}\), and residue classes of the odd quotient \((j+1)/2^t\) modulo \(H\) are equidistributed. Thus each interior gap \(2^{t-1}\) occurs with frequency \(2^{-t}\) per block, when \(1\le t\le k-1\).

When \(v=0\), necessarily \(s=\nu_2(j+1)\ge1\). Conditional on \(s\ge1\), the probability of odd \(s\) is \(2/3\), the probability of even \(s\) is \(1/3\), and the conditional probability of \(q\equiv-1\pmod H\) is \(p=2/H\), independently of \(s\). Equation (2) gives

\[
\Pr(c_j=1\mid v=0)=\frac{1+p}{3}.
\]

Since \(\Pr(v=0)=1/2\), the per-block frequencies of the two gaps for \(v=0\) are \((1+p)/6\) for \(H-1\), and \((2-p)/6\) for \(H\). For \(1\le v\le k-1\), the frequency of gap \(H-2^v\) is \(2^{-v-1}\); for \(v\ge k\), the frequency of \(H/2+1\) is \(2^{-k}\).

It remains to count the optional one-step gap inside a block. The frequency of \(c_j=1\) is

\[
\rho=\Pr(v=0,c_j=1)+\Pr(1\le v<k)
=\frac{1+p}{6}+\frac12-\frac1H
=\frac{2-p}{3}.
\]

Together with the interior one-step gap, whose frequency is \(\Pr(s\ge1)=1/2\), these are precisely the contributions listed for \(\lambda_k\). All densities are obtained from unions of finite residue classes and convergent geometric tails, so the limiting proportions genuinely exist, and all listed types have positive frequency. Every such gap gives a maximal constant run, except for a bounded initial endpoint discrepancy. Adding frequencies yields \(\Lambda_k\), and summing lengths times frequencies yields \(H\), completing the proof.

## Verification

The standalone pure-Python script `verify.py` recomputes the word in two independent ways and tests the exact carry formula, transition locations, spectra and frequency formulas for \(2\le k\le10\). It checks 2,097,152 successive symbols at every tested \(k\), exact initial event sets across at most 4,096 blocks, and run histograms over 32,768 blocks. Rational identities for total mass and length-weighted mass are checked exactly. Run `python3 verify.py` from the directory containing this file. These finite tests are corroboration; steps 1–4 above are the complete infinite proof.

## Relationship to prior work

Abram, Hu and Li (2023; arXiv:2304.14595) treat the broader block-counting family, proving morphicity and algebraicity results rather than classifying maximal runs. Hendel (2025; arXiv:2505.20547, Section 8, Theorem 7) constructs five families of *zero*-run lengths in the same all-one-pattern sequences; those existence assertions are prior work. Hendel's Conjecture 8 explicitly asks whether the list is exhaustive for every \(k\ge3\). The carry-gap theorem here proves that no other zero-run length is possible, and additionally provides the exact all-symbol limiting length distribution. The truth of Conjecture 8 follows when the new exclusion is combined with those existing constructions. Related results about automata, subsequences, or unmodded summatory block counts do not imply the run-transition criterion (1) or the rational length frequencies.

## Limitations

This result concerns the parity of occurrences of a *homogeneous all-one binary pattern*, not arbitrary binary patterns, higher residues, nonconsecutive subsequence patterns, or symbol-resolved separate densities. No general higher-alphabet run-spectrum claim is made. The proof determines all-symbol run lengths and frequencies; the zero-only spectrum uses the previously published existence part of Hendel's Theorem 7. Independent external validation has not been performed. An earlier unindexed equivalent derivation could exist despite the comparisons described in the accompanying review.

## References

1. A. Abram, Y. Hu, S. Li, *Block-counting sequences are not purely morphic*, arXiv:2304.14595 (first public 2023-04-28), later *Advances in Applied Mathematics* **155** (2024), article 102673, DOI:10.1016/j.aam.2024.102673. https://arxiv.org/html/2304.14595v1
2. R. J. Hendel, *Runs, Squares, Palindromes, and Unbordered Factors of a Family of Binary Pattern Sequences with the All-One Pattern*, arXiv:2505.20547 (first public 2025-05-26), Section 8, Theorem 7 and Conjecture 8. https://arxiv.org/html/2505.20547v5
