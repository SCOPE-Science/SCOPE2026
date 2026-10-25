# Sharp two-step absorption and the unique-defect law for random multipermutations

## Finding

Let \(0<p<1\) be fixed. Let \(B_n=(b_{ij})\) be an \(n\times n\) matrix of independent Bernoulli \(p\) entries and take all matrix products in the Boolean semiring. Write \(J_n\) for the all-ones relation, \(q_p=1-p^2\), and \(s_p=1-2p^2+p^3\). Then, as \(n\to\infty\),
\[
 \Pr(B_n^2\ne J_n)\sim n(n-1)s_pq_p^{n-2}.
\]
The same asymptotic holds after conditioning on every row and column being nonempty. Conditional on \(B_n^2\ne J_n\), with probability tending to one, \(B_n^2\) differs from \(J_n\) in **exactly one off-diagonal position**. Given that unique defect is off-diagonal, its location is uniform on the \(n(n-1)\) possible locations.

In particular, let \(M_n\) be the monoid of multipermutations on \([n]\), i.e. all binary relations with nonempty rows and columns, and let \(R_n\) be uniform on \(M_n\). Then
\[
 \Pr(R_n^2\ne J_n)\sim\frac{10}{9}n^2\left(\frac34\right)^n.
\]
Since \(J_n\) is an absorbing element in \(M_n\), almost all multipermutations reach it by the second self-product. The stated sharp asymptotic and unique-defect law, not this qualitative exponent-two phenomenon alone, constitute the finding.

## Assumptions and scope

Binary relations are identified with \(0,1\) adjacency matrices, including diagonal entries (loops). Composition is \((AB)_{ij}=\bigvee_{k=1}^n(a_{ik}\wedge b_{kj})\). A multipermutation is a relation with full domain and full range, equivalent to a matrix having no empty row or column. Asymptotics keep the entry density \(p\) fixed in \((0,1)\); no claim is made for \(p\) depending on \(n\). The proof uses the i.i.d. model first and conditions on full domain and range only at the end. The main asymptotic is for \(n\ge2\), with \(n\to\infty\).

## Proof

Put \(E_{ij}=\{(B_n^2)_{ij}=0\}\). For each intermediate vertex \(k\notin\{i,j\}\), the failure of the two-step walk \(i\to k\to j\) has probability \(1-p^2=q_p\); these failure events are independent over different \(k\). If \(i=j\), the intermediate choice \(k=i\) fails with probability \(1-p\), so
\[
 \Pr(E_{ii})=(1-p)q_p^{n-1}.
\]
If \(i\ne j\), the two intermediate choices \(k=i,j\) jointly fail precisely when \(b_{ij}=0\), or \(b_{ij}=1\) and both \(b_{ii}=b_{jj}=0\). Their joint probability is
\[
 (1-p)+p(1-p)^2=s_p.
\]
They are independent of the other \(n-2\) intermediates. Consequently the expected total number \(D_n=|\{(i,j):(B_n^2)_{ij}=0\}|\) of missing positions is exactly
\[
 \mu_n=\mathbb E D_n=n(n-1)s_pq_p^{n-2}+n(1-p)q_p^{n-1}.
\]
In particular \(\mu_n\sim n(n-1)s_pq_p^{n-2}\), since \(p\) is fixed and \(s_p>0\).

We bound collisions between distinct defect positions. Fix two distinct ordered pairs \((i,j),(u,v)\), and remove their at most four endpoint vertices. For each remaining intermediate vertex \(k\), the two missing-walk conditions depend on independent Bernoulli entries across different \(k\). If the pairs share a source \(i=u\) or target \(j=v\), the probability that neither two-step walk exists through this \(k\) is exactly \(s_p\): the common first (respectively second) arc either is absent, or is present while both other arcs are absent. If they share neither source nor target, the four involved matrix entries are distinct, so the corresponding probability is \(q_p^2\). The constraints at the at most four removed intermediates can only lower the joint probability. Hence
\[
 \Pr(E_{ij}\cap E_{uv})\le
 \begin{cases}
 s_p^{n-4},& i=u\text{ or }j=v,\\
 q_p^{2(n-4)},&i\ne u\text{ and }j\ne v.
 \end{cases}
\]
Here and below a negative exponent at very small \(n\) is irrelevant; we use these bounds for \(n\ge4\). There are at most \(2n^3\) unordered pairs of the first type and at most \(n^4\) of the second type. Since \(0<s_p<q_p<1\),
\[
 \sum_{(i,j)<(u,v)}\Pr(E_{ij}\cap E_{uv})
 =O_p(n^3s_p^{n-4}+n^4q_p^{2n-8})=o(\mu_n).
\]
The first two Bonferroni inequalities therefore yield
\[
 \mu_n-o(\mu_n)\le\Pr(D_n>0)\le\mu_n.
\]
This proves the unconditioned sharp asymptotic. The sum of probabilities of the diagonal events is \(n(1-p)q_p^{n-1}=o(\mu_n)\), and the probability that two or more defect positions occur is at most the same pair-intersection sum, \(o(\mu_n)\). Thus, given \(D_n>0\), the probability of exactly one off-diagonal defect tends to one.

Let \(H_n\) be the event that every row and column of \(B_n\) is nonempty. By the union bound,
\[
 \Pr(H_n^c)\le2n(1-p)^n.
\]
Because \(1-p<1-p^2=q_p\), this error is \(o(\mu_n)\); also \(\Pr(H_n)\to1\). Accordingly \(\Pr(D_n>0\mid H_n)\sim\mu_n\), and the unique-off-diagonal-defect assertion survives conditioning. The distribution of \(B_n\) conditioned on \(H_n\) is uniform on \(M_n\) when \(p=1/2\). Then \(q_{1/2}=3/4\) and \(s_{1/2}=5/8\), yielding the constant \((5/8)/(3/4)^2=10/9\). Simultaneous relabeling preserves both the matrix distribution and the full-domain-and-range condition and acts transitively on off-diagonal positions, proving uniformity of the unique missing position.

Finally \(J_nR=RJ_n=J_n\) for every \(R\in M_n\), because each row and each column of \(R\) is nonempty. In this sense \(J_n\) is the absorbing element. The chance \(R_n=J_n\) is \(1/|M_n|\to0\), so the typical first arrival is at the second self-multiplication.

## Verification

The accompanying standalone `CHECKER.py` exhaustively constructs all \(2^{n^2}\) binary matrices for \(1\le n\le4\), computes Boolean squares directly, and checks the exact finite-sample expectation \(\mathbb ED_n\), diagonal and off-diagonal single-position probabilities, and the partition of smooth matrices into square-universal and other elements. The checker does not assume the theorem's asymptotic and examines \(2+16+512+65536=66066\) matrices. It yields respectively \(1,3,73,6003\) smooth square-universal matrices for \(n=1,2,3,4\) (with \(n=1\) a degenerate boundary case). Its output is included as `CHECKER_OUTPUT.txt`. This finite test does not prove the limit law; the Bonferroni argument above does.

## Relationship to prior work

Carvalho and Martin, *The lattice and semigroup structure of multipermutations* (arXiv:2103.06012, initially public 10 March 2021), define and investigate the same monoid \(M_n\), obtaining structural results on Green relations, regularity and generation. Their accessible complete arXiv text was checked, including its monoid-structure section; it does not state a sharp random-square failure law.

The qualitative fact that almost all \(0,1\) matrices are primitive, indeed with primitive exponent two, is attributed to Moon and Moser (1966) in Brualdi and Ryser, *Combinatorial Matrix Theory*, Section 3.5. Furthermore Shitov, *Almost all Boolean matrices are prime* (2024), quotes earlier work on the Boolean product of two independent random matrices being the all-ones matrix with high probability. These claims are broader background, not novelty claims here; independent products have different dependence from self-squares. The contribution isolated here is the leading probability constant at every fixed density, conditioning on multipermutations, and the unique-off-diagonal-defect description. The Moon–Moser original paper was not inspected in full; its possible quantitative overlap is a substantive priority risk.

## Limitations

The density \(p\) is fixed strictly between zero and one; no sparse or near-complete threshold is established. Only the first-order rare-event probability and typical defect shape are proved, not an exact closed formula for \(\Pr(B_n^2=J_n)\) at arbitrary \(n\). The underlying qualitative exponent-two behavior is classical, and priority for the sharp constant requires further historical verification of the original 1966 article and literature on quantitative random digraph exponents. No independent mathematical audit has been performed.

## References

1. Catarina Carvalho and Barnaby Martin, *The lattice and semigroup structure of multipermutations*, arXiv:2103.06012, first public 2021-03-10. https://arxiv.org/abs/2103.06012
2. J. W. Moon and L. Moser, *Almost all (0,1)-matrices are primitive*, Studia Sci. Math. Hungar. 1 (1966), 153–156. Relevant historical result cited in the reference below; complete original not inspected.
3. Richard A. Brualdi and Herbert J. Ryser, *Combinatorial Matrix Theory*, Cambridge University Press, 1991, Section 3.5 (statement that almost all such matrices have exponent two).
4. Yaroslav Shitov, *Almost all Boolean matrices are prime*, December 2024 preprint, Section 2 (results on products of independent random Boolean matrices and asymptotic semigroup generation). https://doi.org/10.13140/RG.2.2.28902.33603

