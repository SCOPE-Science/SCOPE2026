# Exact online shattering of fixed-length cyclic arcs

## Finding
Let \(n\ge2\) and \(1\le k<n\) be integers. Write \(\mathbb Z_n=\mathbb Z/n\mathbb Z\), and let \(\mathcal A_{n,k}\) consist of the \(n\) characteristic functions of all length-\(k\) cyclic intervals
\[
h_c(x)=\mathbf 1\{(x-c)\bmod n\in\{0,\ldots,k-1\}\},\qquad c,x\in\mathbb Z_n.
\]
Put \(s=\min\{k,n-k\}\). Then
\[
\boxed{\operatorname{Ldim}(\mathcal A_{n,k})=1+\lfloor\log_2 s\rfloor,\qquad
\operatorname{VCdim}(\mathcal A_{n,k})=\begin{cases}1,&s=1,\\2,&s\ge2.\end{cases}}
\]
For a fixed \(n\), the largest possible Littlestone dimension among these classes is \(\lfloor\log_2 n\rfloor\), attained whenever \(s\ge2^{\lfloor\log_2 n\rfloor-1}\). In particular, fixed-length cyclic intervals give an unbounded Littlestone dimension while the VC dimension is at most two.

## Assumptions and scope
The domain and candidate centers both equal the finite cycle \(\mathbb Z_n\); each arc has exactly \(k\) distinct consecutive points. All centers are allowed; there are no restrictions on adaptively chosen query points. Each nontrivial cyclic arc has a unique starting boundary, so the displayed hypotheses are distinct. The Littlestone dimension is the maximal depth of a *complete* binary tree with an instance at each internal vertex such that every root-to-leaf binary labeling is realized by a single hypothesis; the empty-depth tree exists. The VC dimension uses ordinary nonadaptive shattering. These are combinatorial, realizable, deterministic notions, not randomized mistake bounds.

## Proof
**1. Reduction to a short arc.** Replacing every hypothesis \(h\) with \(1-h\) does not change either dimension: flip every label in a shattered tree or shattered trace. The complement of a length-\(k\) cyclic arc is a length-\(n-k\) cyclic arc, with all its translates represented. Therefore it suffices to consider \(k=s\le n/2\).

**2. A universal upper bound on depth.** For every query point \(x\), exactly \(s\) of the \(n\) hypotheses answer \(1\): their centers are the consecutive residues \(x-s+1,\ldots,x\). A complete tree of depth \(d\ge1\) requires at least \(2^{d-1}\) *distinct* hypotheses on its positive root branch, because its \(2^{d-1}\) leaves have mutually incompatible label histories. Consequently \(2^{d-1}\le s\), or \(d\le1+\lfloor\log_2 s\rfloor\). This upper bound holds for every choice of root.

**3. Binary-search lemma for center blocks.** Suppose \(m\le s\), and retain exactly the \(m\) hypotheses whose centers belong to one consecutive block \(C=\{u,u+1,\ldots,u+m-1\}\), read modulo \(n\). For any integer \(0\le t\le m\), the query \(x=u+t-1\pmod n\) (when \(t=0\), interpret \(x=u-1\)) labels the first \(t\) retained centers positive and the remaining \(m-t\) negative. Indeed, the positive centers form the cyclic block \(\{u+t-s,\ldots,u+t-1\}\) of length \(s\). It contains precisely the desired prefix; it cannot wrap around the other side of \(C\), since the union of the two relevant blocks fits inside an unwrapped interval of length at most \(s+m\le2s\le n\). Thus on \(m=2^r\) consecutive centers there exists a complete shattered tree of depth \(r\): split the block into equal halves by this query and recurse.

**4. A matching tree on all hypotheses.** Let \(r=\lfloor\log_2 s\rfloor\), and let \(m=2^r\le s\). Query \(x=s-1\) at the root. The positive-center block is \(\{0,\ldots,s-1\}\), and the negative-center block is \(\{s,\ldots,n-1\}\). Because \(n-s\ge s\ge m\), retain \(m\) consecutive centers in each branch: \(\{0,\ldots,m-1\}\) for the positive branch and \(\{s,\ldots,s+m-1\}\) for the negative branch. Apply the binary-search lemma separately to the two branches, producing complete depth-\(r\) trees. Joining them to the root gives a complete depth-\(r+1\) tree. The upper and lower bounds agree. For fixed \(n\), maximize \(s\le\lfloor n/2\rfloor\) and observe \(1+\lfloor\log_2\lfloor n/2\rfloor\rfloor=\lfloor\log_2 n\rfloor\) for every \(n\ge2\).

**5. VC dimension.** If \(s=1\), the class is the set of all singletons up to complementation; it shatters a single point and no pair. Suppose \(s\ge2\). The adjacent points \(\{a,a+1\}\) are shattered by the arcs beginning at \(a\), ending at \(a\), beginning at \(a+1\), and beginning at \(a+2\), respectively: their traces are \(11,10,01,00\); the latter arc avoids both because \(n\ge2s\ge s+2\). Hence the VC dimension is at least two.

To exclude a shattered triple, consider any three points \(a,b,c\) with an arc of length \(s\) containing all three (the \(111\) trace would require this). Read them in the cyclic order within that arc. The short path from \(a\) to \(c\) passes through \(b\) and uses at most \(s-1\) edges. The other circular path from \(c\) to \(a\) uses at least \(n-s+1\ge s+1\) edges, so no length-\(s\) arc can contain both \(a\) and \(c\) while avoiding \(b\). The \(101\) trace is impossible. Thus no triple is shattered, proving the VC formula.

## Verification
The standalone Python 3 program `cyclic_arcs_verify.py` constructs the hypotheses explicitly as bit masks, evaluates the exact Littlestone minimax recurrence on version spaces, and compares it to the closed formula for every \(2\le n\le16\) and \(1\le k<n\) (120 parameter pairs). It separately checks ten larger near-semicycle parameter pairs through \(n=64\). A distinct trace enumeration checks the VC formula through all triples for all 190 parameter pairs with \(2\le n\le20\).

The same program generates complete shattered trees using the constructive block-halving proof and checks *every* root-to-leaf path in six examples, up to \(n=128\), \(s=64\), depth seven with 128 leaves. The complete final tree is in `cyclic_arcs_witness_n128_k64.json`. Execution results appear in `cyclic_arcs_verification_output.txt`; all tests passed. Running `python3 cyclic_arcs_verify.py` from the artifact directory reproduces the tests and rewrites the deterministic witness file. Finite tests confirm boundary cases but are not offered as a proof for unbounded \(n\); the proof above is uniform.

## Relationship to prior work
Malliaris and Moran (arXiv:2108.05569, initial release 2021-08-12) develop the relationship between Littlestone dimension, finite stability, and VC methods. Their results concern excellent sets, majority and structural learning conditions; they do not state the displayed cyclic-block formula. Malliaris and Moran (arXiv:2212.05050, 2022-12-09) establish general learning-theoretic characterizations of stability and give definitions of Littlestone trees and model-theoretic rank, rather than a rank calculation for fixed-size cyclic arcs. Chase, Freitag and Reyzin (arXiv:2310.04812, 2023-10-07), Section 3, use a class of *pairwise disjoint* real intervals of Littlestone dimension one; their example is structurally distinct from the overlapping translates treated here. The exact calculation is not implied by the general information-theoretic upper bound \(\operatorname{Ldim}(\mathcal H)\le\lfloor\log_2|\mathcal H|\rfloor\), which can be strict: for instance, when \(s=1\) and \(n\) grows, the dimension stays one despite \(n\) hypotheses.

## Limitations
The result is confined to uniform-length arcs on a finite one-dimensional cycle. It does not classify translates of arbitrary disconnected supports, nonuniform arcs, unions of arcs, or randomized optimal mistake bounds. The proof provides exact dimensions without asserting a more general learning theorem. No claim of exhaustive publication priority or independent external verification is made. Broad search and inspected primary literature did not reveal an earlier equivalent exact formula, but an unindexed statement under circular-threshold or sliding-window terminology remains a priority risk.

## References
1. M. Malliaris and S. Moran, *Agnostic Online Learning and Excellent Sets*, arXiv:2108.05569, first public version 2021-08-12; later revised as *Model Theory and Agnostic Online Learning via Excellent Sets*. https://arxiv.org/abs/2108.05569
2. M. Malliaris and S. Moran, *The Unstable Formula Theorem Revisited via Algorithms*, arXiv:2212.05050, first public version 2022-12-09. https://arxiv.org/abs/2212.05050
3. H. Chase, J. Freitag and L. Reyzin, *Applications of Littlestone Dimension to Query Learning and to Compression*, arXiv:2310.04812, first public version 2023-10-07. https://arxiv.org/abs/2310.04812
