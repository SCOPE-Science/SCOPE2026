# Single-crossing laws and sharp total-variation responses to balancing in-degrees of random mappings

## Finding
Let \(n\ge2\) and let \(\boldsymbol d=(d_1,\ldots,d_n)\) be nonnegative integers summing to \(n\). Draw uniformly a mapping \(F:[n]\to[n]\) with exactly \(d_i\) preimages of vertex \(i\). Let \(C\) count the vertices on directed cycles, and let \(B\) count the directed cycles (equivalently the components).

Fix two distinct vertices \(u,v\) with \(a=d_u\ge d_v+2=b+2\). Define a *balancing transfer* by replacing \((a,b)\) with \((a-1,b+1)\) and leaving all other in-degrees unchanged. Primes denote the resulting laws. Write \(h=a-b-1>0\) and \(\boldsymbol q=(d_i:i\notin\{u,v\})\), with \(r\) its number of positive entries. Write \(e_j\) for elementary symmetric polynomials, with \(e_0=1\) and \(e_j=0\) outside their natural range.

**Theorem.** At every integer threshold,
\[
\Pr(C'\ge k)-\Pr(C\ge k)=
\begin{cases}
\displaystyle h\,\frac{e_{k-2}(\boldsymbol q)}{\binom nk},&2\le k\le n,\\
0,&k=1\text{ or }k>n.
\end{cases}
\]
The strict inequalities are precisely at \(2\le k\le r+2\). The signed probability-mass difference \(\Pr(C'=k)-\Pr(C=k)\), after omitting zeros, has *exactly one* sign change, from negative at small \(k\) to positive at large \(k\). For \(2\le k\le r+1\), the mass difference is negative, zero or positive according as
\[
(k+1)e_{k-1}(\boldsymbol q)-(n-k)e_{k-2}(\boldsymbol q)
\]
is positive, zero or negative. Consequently
\[
d_{\mathrm{TV}}(\mathcal L(C'),\mathcal L(C))
=h\max_{0\le j\le r}\frac{e_j(\boldsymbol q)}{\binom n{j+2}}.
\]
The same one-crossing negative-to-positive conclusion holds for \(\Pr(B'=\ell)-\Pr(B=\ell)\); in particular \(B'\) strictly stochastically dominates \(B\) at at least one nontrivial threshold, and its total-variation distance is no greater than that for \(C\).

Put \(t=\sum_iq_i=n-a-b\), necessarily \(0\le t\le n-2\). Among all nonnegative integral \(\boldsymbol q\) of length \(n-2\) and sum \(t\), the following *sharp universal envelope* holds:
\[
d_{\mathrm{TV}}(\mathcal L(C'),\mathcal L(C))
\le h\max_{0\le j\le t}\frac{\binom tj}{\binom n{j+2}}.
\]
Equality is attained when \(\boldsymbol q\) consists of \(t\) ones and \(n-2-t\) zeros. The maximizing \(j\) is \(\min\{t,\lfloor 2(t+1)/(n-t)\rfloor\}\); if \(2(t+1)/(n-t)\) is an integer between \(1\) and \(t\), the preceding index ties.

This is not, in general, a likelihood-ratio ordering: for \(n=5\), transferring \((3,2,0,0,0)\) into \((3,1,1,0,0)\) gives the cyclic-count masses \((2/5,3/5,0,0,0)\) and \((3/10,2/5,3/10,0,0)\), whose initial likelihood ratio drops from \(3/4\) to \(2/3\). Exhaustive finite checks find no smaller-order counterexample.

## Assumptions and scope
Mappings can have fixed points and multiple preimages, but every vertex has one outgoing edge. All probabilities are conditional on the *entire labeled in-degree sequence*, not merely on an exchangeable or averaged degree model. The elementary transfer requires integers \(a\ge b+2\); no asymptotic approximation is used. When \(r=0\), the one-crossing statement means a negative difference at count one and a positive difference at count two. The bound's optimization is over \(\boldsymbol q\) with the transferred pair \((a,b)\) held fixed. The stochastic comparison extends to any finite sequence of balancing transfers by transitivity, but the exact single-transfer formula applies to one transfer at a time.

## Proof
**1. Known cyclic-set enumeration, restated.** Hansen and Jaworski's multiset-Prüfer encoding [1, Theorem 1 and its proof; 2, pp. 109–111] establishes, for a prescribed in-degree vector and a set \(S\subseteq[n]\) of size \(1\le k<n\),
\[
\Pr(\text{cyclic vertex set}=S)
=\frac{\prod_{i\in S}d_i}{(n-k)\binom nk}
\sum_{i\in S}(d_i-1).
\]
For \(1\le k<n\), summing over \(S\) and using \(\sum_i d_i=n\) gives
\[
\Pr(C=k)=\frac{e_k(\boldsymbol d)}{\binom nk}-
\frac{e_{k+1}(\boldsymbol d)}{\binom n{k+1}}.
\]
At \(k=n\), one instead has \(\Pr(C=n)=e_n(\boldsymbol d)\): this equals one if all degrees are one and zero otherwise. With \(\Pr(C\ge n+1)=0\), telescoping yields the **previously available** identity \(\Pr(C\ge k)=e_k(\boldsymbol d)/\binom nk\). This base identity is not presented as novel.

**2. Exact effect of a transfer.** The elementary-symmetric generating polynomial factorizes as
\[
\prod_i(1+d_iz)=(1+az)(1+bz)\prod_i(1+q_iz).
\]
A balancing transfer fixes \(a+b\) and increases \(ab\) by \(h=a-b-1\). Hence \(e_k(\boldsymbol d')-e_k(\boldsymbol d)=h e_{k-2}(\boldsymbol q)\), proving the tail formula, strictness and the mass sign test.

**3. Strict unimodality and sharp distance.** Set \(A_j=e_j(\boldsymbol q)/\binom n{j+2}\) for \(0\le j\le r\), and zero outside this range. Newton's normalized inequalities for \(e_j\) in \(m=n-2\) variables imply at \(1\le j<r\)
\[
\frac{A_j^2}{A_{j-1}A_{j+1}}
\ge\frac{(j+1)(j+2)}{j(j+3)}>1.
\]
Indeed the usual Newton bound introduces the factor \(\frac{(j+1)(m-j+1)}{j(m-j)}\); the binomial denominators contribute \(\frac{(j+2)(n-j-2)}{(j+3)(n-j-1)}\), and \(m\le n-2\) gives the displayed strict lower bound. Thus the positive sequence \(A_j\) is strictly log-concave and has one unimodal peak or two adjacent tied peaks. The mass differences are \(h(A_{k-2}-A_{k-1})\), where \(A_{-1}=A_{r+1}=0\); they therefore change sign exactly once after zeros are omitted. The total variation of two stochastically ordered laws with a single mass sign crossing equals their maximum tail discrepancy, yielding the stated identity.

**4. Component-count sign variation.** Conditional on \(C=k\), the cycle restriction is a uniform permutation of its \(k\) cyclic vertices, because every permutation on a fixed cyclic set leaves the multiplicity count of attached forests unchanged. Consequently \(B\mid C=k\) is the number of cycles in a uniformly random permutation of \(k\) symbols. Its probability kernel is \(K(k,\ell)=c(k,\ell)/k!\), with \(c(k,\ell)\) unsigned Stirling numbers of the first kind. The generating polynomial \(\prod_{i=1}^k(t+i-1)/i\) is real-rooted, hence its positive coefficient row is log-concave. The recurrence
\[
K(k+1,\ell)=\frac{k}{k+1}K(k,\ell)+\frac1{k+1}K(k,\ell-1)
\]
then shows that \(K(k+1,\ell)/K(k,\ell)\) is nondecreasing in \(\ell\), using the natural zero-support convention. Therefore \(K\) is totally positive of order two. Split the single-crossing signed difference of the two laws of \(C\) into an equal-mass negative part supported on lower \(k\) and a positive part supported on higher \(k\). Their images under \(K\) are likelihood-ratio ordered; subtracting gives at most one mass sign change, and it is negative-to-positive. Strict negativity at \(\ell=1\) follows from \(K(k,1)=1/k\) being strictly decreasing, and the mass sums to zero, so a positive entry also occurs. A Markov kernel cannot increase total variation, proving contraction.

**5. Sharp envelope and its index.** Regard each of the \(t\) integer units in the coordinates of \(\boldsymbol q\) as distinguishable. The weight \(e_j(\boldsymbol q)\) counts \(j\)-subsets of these units that lie in distinct coordinates, so \(e_j(\boldsymbol q)\le\binom tj\), with equality simultaneously for every \(j\) if every coordinate is zero or one. Finally the successive ratio of \(U_j=\binom tj/\binom n{j+2}\) is
\[
\frac{U_j}{U_{j-1}}=\frac{(t-j+1)(j+2)}{j(n-j-1)},
\]
which is at least one exactly when \(j\le 2(t+1)/(n-t)\). This locates all maximizing indices and completes the proof.

## Verification
Run the accompanying `verify_mapping.py` with a standard Python interpreter (no third-party packages). It uses exact rational arithmetic, exhaustively enumerates all labeled mappings for orders \(2\) through \(7\), and verifies the cyclic and component distributions under every realized labeled degree sequence. For integer-partition representatives through order \(11\), it tests every elementary balancing transfer, the tail identity, the one-crossing property for both statistics, the total-variation formula and sharp upper envelope. It also checks the explicit five-vertex likelihood-ratio counterexample. Observed result: `PASS exact_assertions=91476 enumerated_mappings=873611 distinct_labeled_indegrees=2352 elementary_transfers=2438 exhaustive_mapping_n=2..7 transfer_partitions_n=2..11 LR_first_counterexample_n=5`. All-size correctness rests on the proof, not the finite checks.

## Relationship to prior work
Hansen and Jaworski [1, 2] developed the prescribed/exchangeable-in-degree mapping model, proved the base cyclic-point distribution and described the Stirling cycle-count transform. These are **prior results**. The present contribution is the exact response to a degree transfer, its strict single-crossing and sharp total-variation conclusions, the inherited component-count sign variation, the optimal integer-profile envelope and the boundary counterexample to likelihood-ratio strengthening. Their later restricted-in-degree structural-transition study [3] examines exact and asymptotic cycle counts for families with degree caps rather than deterministic pairwise degree transfers. Classical Newton inequalities and real-rootedness of Stirling cycle polynomials are used as ingredients; neither alone is asserted as new.

## Limitations
The local results are for deterministic integer in-degree vectors and direct one-unit balancing moves. Arbitrary mixtures of vectors or random mappings with independent but unequal target probabilities are not covered. The distributional one-crossing result is weaker than likelihood-ratio ordering, which fails in the displayed example. A prior result expressed through equivalent total-positivity or symmetric-function inequalities might implicitly contain this theorem; checking historical priority cannot be exhaustive. Independent external mathematical validation has not been performed.

## References
[1] J. C. Hansen and J. Jaworski, *A new random mapping model*, arXiv:math/0603529, first posted 22 March 2006, https://arxiv.org/abs/math/0603529.

[2] J. C. Hansen and J. Jaworski, *Random Mappings With Exchangeable In-Degrees*, Random Structures & Algorithms 33 (2008), 105–126, first online 4 September 2007, https://doi.org/10.1002/rsa.20187.

[3] J. C. Hansen and J. Jaworski, *Structural Transition in Random Mappings*, Electronic Journal of Combinatorics 21(1) (2014), #P1.18, https://doi.org/10.37236/3572.
