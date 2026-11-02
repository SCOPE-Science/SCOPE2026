# A finite-group limit law for coloured unary permutations

## Finding

Let \(q\geq2\) be fixed. Sample uniformly a labelled \(n\)-element structure with one **bijective unary operation** and exactly one of \(q\) named, mutually exclusive colours on each element. Its automorphism group, viewed up to abstract group isomorphism, converges **in total variation** to the explicit finite random group described below. In particular, its automorphism-group order stays tight, although the number of permutation cycles diverges.

Let \(\mathcal N_q\) be the set of all necklaces (cyclic-rotation classes) of finite nonempty words over the \(q\)-colour alphabet. For a necklace \(w\), write \(\ell(w)\) for its length and \(s(w)\) for the number of rotations fixing it; thus \(s(w)\mid\ell(w)\). Take independent variables
\[
Z_w\sim\operatorname{Poisson}\!\left(\frac{1}{s(w)q^{\ell(w)}}\right),\qquad w\in\mathcal N_q.
\]
With \(C_s\) a cyclic group of order \(s\), and \(S_m\) the symmetric group on \(m\) points, put
\[
\mathcal G_q=\prod_{w\in\mathcal N_q}\bigl(C_{s(w)}\wr S_{Z_w}\bigr),
\]
where factors of order one are omitted. **Only finitely many factors are nontrivial almost surely**, so this is a finite group. If \(G_{n,q}\) denotes the actual automorphism group of the random structure, then
\[
\boxed{d_{\mathrm{TV}}\bigl(\mathcal L(G_{n,q}),\mathcal L(\mathcal G_q)\bigr)\longrightarrow0.}
\]

The order-two stratum has an exact labelled enumeration. Define the number of primitive \(q\)-ary necklaces of length \(d\) by
\[
p_q(d)=\frac1d\sum_{e\mid d}\mu(e)q^{d/e}.
\]
If \(t_{q,n}\) counts the labelled structures with automorphism group of order exactly two, then, as a formal power-series identity,
\[
\boxed{
T_q(z):=\sum_{n\geq0}\frac{t_{q,n}}{n!}z^n
=\frac{1-qz^2}{2(1-qz)}
\sum_{d\geq1}p_q(d)z^{2d}\left(1+\frac{1}{1+z^d}\right).
}
\]
For every fixed \(q\geq2\), the fraction of the total \(q^n n!\) structures with exactly two automorphisms converges exponentially fast to
\[
\boxed{
c_q=\left(1-\frac1q\right)\frac12\sum_{d\geq1}p_q(d)q^{-2d}
\left(1+\frac{1}{1+q^{-d}}\right)>0.
}
\]
The sum is absolutely convergent; for \(q=2\), \(c_2=0.261848236423527184\ldots\). The large-colour expansion is \(c_q=q^{-1}-q^{-2}+\tfrac13q^{-3}+O(q^{-4})\). The rigidity fraction equals exactly \(1-1/q\) for every \(n\geq2\), a **previously known** Lyndon-factorization identity [2], not a novelty claim here.

There is a sharp one-colour contrast: for \(q=1\), \(\lvert G_{n,1}\rvert\to\infty\) in probability, and the order-two EGF reduces to \(T_1(z)=z^2+z^3/2\); no structure on \(n\geq4\) points has exactly two automorphisms.

## Assumptions and scope

For each \(n\geq1\), the carrier is \([n]\); choose \(f:[n]\to[n]\) uniformly among the \(n!\) permutations, and independently choose \(\kappa:[n]\to[q]\) uniformly among the \(q^n\) colourings. An automorphism is a permutation \(g\) satisfying \(gf=fg\) and \(\kappa\circ g=\kappa\). The parameter \(q\) is fixed while \(n\to\infty\). The group space is the countable discrete space of isomorphism classes of finite groups, not a topology on group actions. The empty structure is introduced only as the constant term of generating functions.

A necklace is **primitive** if its only stabilizing rotation is the identity, or \(s(w)=1\). A word of length \(\ell\) with least period \(d\) has \(s=\ell/d\). The trivial wreath factors use \(S_0=S_1=\{1\}\) when appropriate; the empty direct product is trivial. The expressions involving \(p_q(d)\) are integer-valued for all positive integers \(q,d\).

## Proof

**1. Cycle-type automorphism decomposition.** Every cycle of \(f\) carries a cyclic colour word and therefore a unique necklace \(w\). Suppose \(m_w\) cycles have necklace \(w\). A colour-preserving automorphism commuting with \(f\) may permute these \(m_w\) cycles arbitrarily, and, independently, rotate each cycle by one of the \(s(w)\) colour-preserving rotations. Different necklace types cannot be interchanged. Hence, for every finite structure,
\[
\operatorname{Aut}([n],f,\kappa)\cong
\prod_w\bigl(C_{s(w)}\wr S_{m_w}\bigr),\qquad
\lvert\operatorname{Aut}\rvert=\prod_w s(w)^{m_w}m_w!.
\]
This proves the exhaustive classification of possible sources of nontrivial symmetry.

**2. Exact small-component laws.** For a fixed necklace \(w\) of length \(\ell\) and rotational stabilizer size \(s\), the number of coloured cyclic arrangements of that type on a fixed \(\ell\)-set is \((\ell-1)!\,(\ell/s)=\ell!/s\). Its labelled exponential generating function (EGF) is therefore \(z^{\ell}/s\). Summing over all types gives the unrestricted EGF
\[
\exp\!\left(\sum_{\ell\geq1}\frac{q^\ell z^\ell}{\ell}\right)
=\frac{1}{1-qz}.
\]
For distinct necklaces \(w_1,\ldots,w_a\) and indeterminates \(u_1,\ldots,u_a\), the exact probability generating function for their component multiplicities is
\[
\mathbb E\prod_{i=1}^a u_i^{m_{w_i}}
=\frac{[z^n](1-qz)^{-1}
\exp\left(\sum_{i=1}^a (u_i-1)z^{\ell(w_i)}/s(w_i)\right)}{q^n}.
\]
For any entire function \(F\), \(q^{-n}[z^n](F(z)/(1-qz))\to F(1/q)\). Consequently the multiplicities of every fixed finite set of necklaces converge jointly to independent Poisson variables with means \(1/(s(w)q^{\ell(w)})\). This is also immediate from exact joint factorial moments once \(n\) exceeds the total length of the specified cycles.

**3. Uniformly negligible large symmetries.** Write \(E_{>L}\) for the event that a cycle of length greater than \(L\) participates in a nontrivial automorphism. Such an event requires either a nonprimitive cyclic colour word on some long cycle, or two cycles of the same primitive necklace of the same long length. At length \(\ell\), the number of nonprimitive linear colour words is at most \(\ell q^{\ell/2}\), because every proper word period is at most \(\ell/2\). Since a uniform permutation has expected \(1/\ell\) cycles of length \(\ell\),
\[
\Pr(\text{some nonprimitive cycle of length }>L)
\leq\sum_{\ell>L}q^{-\ell/2}.
\]
For a fixed primitive necklace \(w\) of length \(\ell\), the expected number of unordered pairs of its component cycles is at most \(q^{-2\ell}/2\): the exact value holds when \(2\ell\leq n\), and otherwise is zero. There are \(p_q(\ell)\leq q^\ell/\ell\) such necklaces. Hence
\[
\Pr(\text{a repeated primitive type of length }>L)
\leq\frac12\sum_{\ell>L}\frac{q^{-\ell}}{\ell}.
\]
Both bounds hold uniformly in \(n\) and tend to zero as \(L\to\infty\). The same estimates apply to the independent Poisson variables, using \(\Pr(Z_w\geq2)\leq\mathbb E\binom{Z_w}{2}\) and \(\Pr(Z_w\geq1)\leq\mathbb E Z_w\). Therefore the infinite product defining \(\mathcal G_q\) has almost surely only finitely many nontrivial factors. Truncate all factors to lengths at most \(L\). Step 2 gives convergence in total variation for these finite collections of discrete random variables, hence for their associated finite groups. Uniform tail bounds then give convergence in total variation for the full groups.

**4. Exact rigid and order-two enumeration.** Let \(R_q(z)\) be the EGF of rigid coloured permutations. Step 1 shows that all component necklaces must be primitive and pairwise distinct, so
\[
R_q(z)=\prod_{d\geq1}(1+z^d)^{p_q(d)}.
\]
The elementary necklace identity \(\sum_{d\mid m}d\,p_q(d)=q^m\) implies the formal Witt product \(\prod_{d\geq1}(1-z^d)^{-p_q(d)}=(1-qz)^{-1}\). Replacing \(z\) by \(z^2\) gives
\[
R_q(z)=\frac{1-qz^2}{1-qz}.
\]
The corresponding coefficient identity for rigid objects is already explicitly proved via strictly decreasing Lyndon factorizations in [2].

By Step 1, an automorphism group of order two occurs **in exactly one** of two mutually exclusive ways, all other components being distinct primitive necklaces: (i) two cycles of one primitive necklace \(w\) of length \(d\), which gives a transposition of the two cycles and weight \(z^{2d}/2!\), replacing the factor \(1+z^d\); or (ii) a single cycle with exactly two stabilizing rotations, obtained by repeating a primitive length-\(d\) necklace twice, of weight \(z^{2d}/2\), disjoint from the primitive components. Thus
\[
T_q(z)=R_q(z)\sum_{d\geq1}p_q(d)
\left(\frac{z^{2d}}{2(1+z^d)}+\frac{z^{2d}}2\right),
\]
which is the stated EGF. No third mechanism can give automorphism-group order two because \(s^{m}m!\geq3\) or two independent nontrivial factors force order at least four.

**5. Limiting order-two proportion.** Put \(B_q(z)=\tfrac12\sum_{d\geq1}p_q(d)z^{2d}(1+(1+z^d)^{-1})\). Since \(p_q(d)\leq q^d/d\), this series is analytic throughout \(|z|<q^{-1/2}\); the factors \(1+z^d\) have no zero there. For fixed \(q\geq2\), the function \(H_q(z)=(1-qz^2)B_q(z)\) is analytic in a disc strictly larger than \(|z|\leq1/q\), and \(T_q(z)=H_q(z)/(1-qz)\). Therefore
\[
q^{-n}[z^n]T_q(z)=\sum_{j=0}^n [z^j]H_q(z)q^{-j}
\longrightarrow H_q(1/q)=c_q.
\]
Cauchy estimates show convergence at rate \(O_{q,\lambda}(\lambda^n)\) for every \(q^{-1/2}<\lambda<1\). Expansion of the \(d=1,2,3\) terms, with larger lengths contributing \(O(q^{-4})\), yields the displayed large-\(q\) expansion. The summand is strictly positive, so \(c_q>0\).

**6. The one-colour boundary.** For \(q=1\), only one primitive necklace exists (length one). The preceding EGF identity reduces to \(T_1(z)=z^2+z^3/2\). Furthermore \(f\) itself belongs to the automorphism group of the uncoloured structure, so its order is at least the length of the longest cycle of \(f\). A uniform permutation has expected \(\sum_{j=1}^n1/j\) cycles. Markov's inequality shows that with probability tending to one, there are fewer than \(\sqrt n\) cycles; hence the longest has length greater than \(\sqrt n\). Thus \(\lvert G_{n,1}\rvert\to\infty\) in probability.

## Verification

Run `python checker.py` in the directory containing this document. The standard-library checker independently enumerates all labelled permutations and colourings for \(q=1\) through \(n=5\), \(q=2\) through \(n=5\), and \(q=3\) through \(n=4\), and explicitly tests every commuting, colour-preserving relabelling. It compares group orders against the necklace/wreath expression and compares the order-two counts against the EGF coefficients. It also enumerates primitive necklaces through length six, checks the first additional binary EGF coefficient, and evaluates \(c_2\) with a rigorous omitted-tail upper bound below \(10^{-25}\).

The first binary labelled counts \(t_{2,n}\), for \(n=2,3,4,5,6\), are \(4,18,96,1080,11880\). The limiting value is \(0.261848236423527184\ldots\); these calculations are checks, not an infinite proof. In particular, neither finite enumeration nor a truncated numerical series certifies convergence in total variation: the uniform tail estimates and exact finite-dimensional convergence prove that part.

## Relationship to prior work

Kuželka [1] motivates automorphism-sensitive model counting with genuine unary functions; the present scope is the probabilistic isomorphism-group distribution for a **bijective** unary function and named colours. Band, Harrison, and Sepanski [2] already count strictly decreasing Lyndon decompositions and thereby establish the exact rigid coefficient \((q-1)q^{n-1}\), so rigidity alone is **not new**. Their primitive pseudo-orbit calculation does not present the order-two symmetry mechanisms or the group-valued total-variation limit. The independent-Poisson phenomenon for short permutation cycles is classical and closely related to Ercolani and Ueltschi [3]; Step 3 adds the uniform negligibility of long nontrivial automorphisms required to pass from finite-dimensional cycle counts to an entire group law. This theorem is a specific finite-model symmetry distribution, not a general result about all unary functions, arbitrary relations, or a first-order zero-one law.

## Limitations

The source-based originality conclusion is limited to the materials actually inspected. Standard permutation-cycle Poisson limits and the 2016 Lyndon enumeration are essential prior ingredients; an earlier publication combining these into the same group-valued law or the exact order-two EGF would supersede part of this contribution. No independent historical-priority or mathematical audit is claimed. A portion of the 2026 motivating paper beyond its accessible abstract, contents, and opening material could not be read in this session. The distribution requires fixed \(q\) and a uniformly sampled **permutation**, not an unrestricted random unary operation. The statements concern automorphism-group isomorphism types, not canonically labelled group actions.

## References

[1] O. Kuželka, *Unary Functions, Automorphisms, and Unlabeled First-Order Model Counting*, arXiv:2608.30580v1, first submitted 2026-08-31. https://arxiv.org/abs/2608.30580

[2] R. Band, J. M. Harrison, and M. Sepanski, *Lyndon word decompositions and pseudo orbits on q-nary graphs*, arXiv:1610.03808v1, first submitted 2016-10-12, especially Theorem 2 and Lemma 2. https://arxiv.org/abs/1610.03808

[3] N. M. Ercolani and D. Ueltschi, *Cycle structure of random permutations with cycle weights*, Random Structures & Algorithms 44 (2014), 109–133, first published online 2012-05-07. https://doi.org/10.1002/rsa.20430
