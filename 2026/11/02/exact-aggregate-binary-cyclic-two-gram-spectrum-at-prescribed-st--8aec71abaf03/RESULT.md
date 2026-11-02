# Exact aggregate binary cyclic two-gram spectrum at prescribed strand lengths

## Finding

Consider a collection of oriented binary cycles of prescribed lengths \(n_1,\ldots,n_r\ge2\). Their aggregate observation is the multiset of all cyclic length-two reads, counted across all cycles without retaining the source-cycle labels. Let \(N=\sum_i n_i\), \(S=\sum_i\lfloor n_i/2\rfloor\), and write the observed multiplicities as \((N_{00},N_{01},N_{10},N_{11})\).

**Complete all-length characterization.** Exactly the profiles
\[
 (N_{00},N_{01},N_{10},N_{11})=(A,T,T,N-2T-A)
\]
are possible where either \(T=0\) and \(A\) is a subset sum of the strand lengths, or \(1\le T\le S\) and the integer \(A\) belongs to at least one interval
\[
 \left[\sum_{j\in K}n_j,\ \sum_{j\in K}n_j+\sum_{i\in J}(n_i-2t_i)\right]\cap\mathbb Z.
\]
Here \(J\ne\varnothing\) is the set of nonconstant cycles, \(K\subseteq[r]\setminus J\) is the set of constant-zero cycles, and integers \(1\le t_i\le\lfloor n_i/2\rfloor\) for \(i\in J\) satisfy \(\sum_{i\in J}t_i=T\); every remaining cycle is constant one. Every profile in these intervals has an explicit realizing collection of cycles.

**Sharp universal full-layer threshold.** For each \(r\le T\le S\), every balanced nonnegative profile \((A,T,T,N-2T-A)\) with \(0\le A\le N-2T\) occurs. The threshold \(T=r\) is sharp uniformly over strand-length choices: for \(r\ge2\), taking all \(n_i=2\) leaves the profile \((1,r-1,r-1,1)\) unrealizable at \(T=r-1\), although \((0,r-1,r-1,2)\) and \((2,r-1,r-1,0)\) occur.

**Exact two-strand capacity.** When \(r=2\), let \(n_1,n_2\ge2\), \(N=n_1+n_2\), and \(S=\lfloor n_1/2\rfloor+\lfloor n_2/2\rfloor\). At \(T=0\) the attainable values of \(A\) are \(0,n_1,n_2,N\). At \(T=1\), every \(0\le A\le N-2\) is attainable except the single value \(A=n_1-1\) when \(n_1=n_2\). At each \(2\le T\le S\) every \(0\le A\le N-2T\) occurs. Hence the number of distinct observations, and equivalently the maximum number of pairwise distinguishable two-cycle messages (one source per observation), is
\[
 \boxed{C(n_1,n_2)=S(N-S)+4-2\mathbf1_{\{n_1=n_2\}}.}
\]
These statements concern **aggregate** cyclic reads; they do not assert reconstruction of both cycles individually from an arbitrary shared profile.

## Assumptions and scope

The binary alphabet is \(\{0,1\}\). Cycles are finite, nonempty and indexed by prescribed lengths \(n_i\ge2\); read positions wrap cyclically, even for period-one constant cycles. A pair with the same aggregate multiset is indistinguishable by this observation channel, regardless of whether its constituent cycles are rotations of each other. The number of observations is the exact zero-error code size when codewords may be arbitrary ordered collections of cycles of those prescribed lengths and each codeword receives the deterministic aggregate profile. The formula has no probabilistic or sequencing-error assumptions.

## Proof

**1. Flow balance.** On any circular binary word, every run of zeroes begins with a \(10\) transition and ends with a \(01\) transition. Therefore \(N_{01}=N_{10}\). The same follows by telescoping \(\sum_i(w_{i+1}-w_i)=0\). Write this common count as \(t\) for one cycle. Since every transition consumes a different cyclic adjacency, a nonconstant cycle has \(t\ge1\), contains exactly \(t\) positive zero runs and \(t\) positive one runs, and so \(2t\le n\). A constant cycle has \(t=0\).

**2. Exact one-cycle range.** If \(t=0\), the only possibilities are \(0^n\) and \(1^n\), giving respectively \(N_{00}=n\) and \(0\). For each \(1\le t\le\lfloor n/2\rfloor\), write \(A=N_{00}\) and \(B=N_{11}\). Each of the \(t\) positive zero runs contributes its length minus one to \(A\), and each one run similarly contributes to \(B\). Thus \(A,B\ge0\) and \(A+B=n-2t\). Conversely, for **every** integer \(A\in[0,n-2t]\), put \(B=n-2t-A\). The cyclic word
\[
 0^{A+1}1^{B+1}(01)^{t-1}
\]
has length \(n\), exactly \(t\) runs of each letter, and counts \(N_{00}=A\), \(N_{01}=N_{10}=t\), \(N_{11}=B\). This proves that there are no additional local restrictions.

**3. All-cycle characterization.** For each component, choose its transition number \(t_i\). Let \(J=\{i:t_i>0\}\). If the total \(T=0\), every cycle is constant and the total \(N_{00}\) is exactly a subset sum \(A=\sum_{i\in K}n_i\). For \(T>0\), let \(K\) index those constant cycles that are all zero, while other constant cycles are all one. Their contribution to \(A\) is the base \(\sum_{j\in K}n_j\). For each \(i\in J\), Step 2 permits every integral \(A_i\) in \([0,n_i-2t_i]\). Sums of independent integral intervals fill the entire integral interval with the summed endpoints. This gives precisely the union displayed in the finding, both necessary and sufficient, and the explicit local words in Step 2 can be concatenated as a collection of cycles to realize every profile.

**4. Universal full layer and sharp boundary.** Each capacity \(c_i=\lfloor n_i/2\rfloor\) is at least one. Every integer \(T\) with \(r\le T\le\sum_i c_i=S\) can be written \(T=\sum_i t_i\), where \(1\le t_i\le c_i\), by starting with \(t_i=1\) and distributing \(T-r\) extra units among capacities \(c_i-1\). All cycles are then active, and Step 3 provides every \(A\) in \([0,\sum_i(n_i-2t_i)]=[0,N-2T]\). If instead \(n_i=2\) for all \(i\), at \(T=r-1\) precisely \(r-1\) cycles must each have one transition, contributing no equal-adjacency edges; the remaining length-two cycle must be constant and contributes either \(0\) or \(2\) to \(A\), never \(1\). This proves the uniform threshold cannot be lowered.

**5. Two-strand layer analysis.** At \(T=0\), Step 3 gives precisely the multiset of values \(\{0,n_1,n_2,N\}\), with four distinct values unless \(n_1=n_2\), when it has three. At \(T=1\), exactly one cycle is active. If the first is active, its \(A\)-range is \([0,n_1-2]\) when the second is constant one, and \([n_2,N-2]\) when the second is constant zero; reversing roles contributes \([0,n_2-2]\) and \([n_1,N-2]\). Their union is
\[
 [0,\max(n_1,n_2)-2]\cup[\min(n_1,n_2),N-2]
\]
on the integers. When the lengths differ, this union is full, since their difference is at least one. When they agree at \(n_1=n_2=s\), the unique gap is \(A=s-1\). All \(T\ge2\) up to \(S\) use Step 4 with both cycles active. Summing the sizes \(N-2T+1\) of fully attainable positive layers gives
\[
 \sum_{T=1}^{S}(N-2T+1)=S(N-S).
\]
The \(T=0\) layer contributes \(4-\mathbf1_{\{n_1=n_2\}}\) profiles, while the \(T=1\) layer loses \(\mathbf1_{\{n_1=n_2\}}\) from the full-layer sum. This yields the boxed exact formula.

**6. Information-theoretic interpretation.** Every source collection maps to exactly one aggregate profile. A set of messages distinguishable without error can contain no two sources having the same profile, so its size is at most the number \(C(n_1,n_2)\) of realizable profiles. Conversely, Step 3 constructs at least one valid source collection for each profile; selecting one per profile gives a code meeting the bound. No claim about correcting missing/erroneous reads is made.

## Verification

Run `python3 VERIFY.py`. The standalone standard-library checker enumerates all binary cycles for every ordered two-strand length pair in \(\{2,\ldots,9\}^2\) (64 cases), all three-strand length tuples in \(\{2,\ldots,5\}^3\) (64 cases), and all four-strand tuples in \(\{2,3,4\}^4\) (81 cases). It compares directly enumerated aggregate cyclic pairs with the interval construction, checks the exact two-strand profile formula and every predicted capacity, and verifies the sharp obstruction for \(2\le r\le12\) with all strand lengths two. Expected output:

```
VERIFY_OK two_length_pairs=64 triple_length_tuples=64 quadruple_length_tuples=81 sharpness_k=2..12
```

These finite checks corroborate the proof. The all-length conclusion follows from Steps 1–6, not extrapolation from enumeration.

## Relationship to prior work

Tesler's *Multi de Bruijn Sequences* (2017) develops Eulerian, linearized and multicyclic descriptions of prescribed read multiplicities, including counting decompositions without prescribing the individual component lengths. Here **every component length is fixed**, and the objective is the attainable support of the *aggregate binary two-read observation*, with an exact length-equality defect and explicit two-strand zero-error capacity. Arbitrary-cycle decomposition enumeration alone does not state the fixed-length-layer classification. Yehezkeally, Marcovich and Yaakobi's *Multi-strand Reconstruction from Substrings* (2021) studies simultaneous reconstruction and coding from multisets of **linear substring reads** with different asymptotic length regimes. Kiah, Puleo and Milenkovic's *Codes for DNA Sequence Profiles* (2015) supplies the broader sequence-profile/de Bruijn-flow coding viewpoint, mainly for one linear source. The fixed-length multi-cycle profile theorem here is not the general counting theorem of those sources, though general cycle-flow methods are closely related.

## Limitations

The classification assumes a binary alphabet, noiseless complete length-two read multiplicities, and known component lengths each at least two. It counts **distinguishable aggregate profiles**, not distinct reconstructions inside a profile fiber. It does not address strand-length uncertainty, longer reads, arbitrary alphabets, noisy observations or more efficient code constructions. In broader Eulerian-flow and multistrand literature, a reformulation of the same special case may exist; an independent literature audit remains outstanding.

## References

- Glenn Tesler, *Multi de Bruijn Sequences*, arXiv:1708.03654, first publicly posted 2017-08-11, https://arxiv.org/abs/1708.03654.
- Yonatan Yehezkeally, Sagi Marcovich and Eitan Yaakobi, *Multi-strand Reconstruction from Substrings*, arXiv:2108.11725, first publicly posted 2021-08-26, https://arxiv.org/abs/2108.11725.
- Han Mao Kiah, Gregory J. Puleo and Olgica Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517 (background on linear-source profiles), https://arxiv.org/abs/1502.00517.
