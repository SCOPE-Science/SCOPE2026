# Convex subalgebras and random generation of finite S4-chain algebras

## Finding
Let \(n\geq1\), and form the full complex algebra \(\mathcal A_n\) of the reflexive linear frame \(0\leq1\leq\cdots\leq n-1\), with Boolean operations and \(\Diamond X=\{i:\exists j\geq i,\ j\in X\}\). Every modal Boolean subalgebra is the family of unions of the intervals in one unique consecutive-block partition. Thus its subalgebra lattice is the Boolean lattice on the \(n-1\) adjacent cuts, with exactly \(2^{n-1}\) members.

For any ordered \(k\)-tuple of generators \(G_1,\ldots,G_k\), where \(k\geq0\), label each world by its \(k\)-bit membership word. Write \(r\) for the number of maximal consecutive runs of identical words. The generated subalgebra is **exactly** the set of unions of these \(r\) runs, of cardinality \(2^r\). Put \(m=2^k\). For each \(1\leq r\leq n\), the exact number of labelled generator tuples whose generated algebra has \(2^r\) elements is
\[
 m\binom{n-1}{r-1}(m-1)^{r-1}.
\]
When \(m=1\) and \(r=1\), the empty product \((m-1)^0\) is interpreted as one.

For independent uniformly random generator subsets, the number \(Z=n-r\) of collapsed boundaries has law \(\mathrm{Bin}(n-1,2^{-k})\). The exact probability of generation of the full algebra is
\[
\Pr\bigl(\langle G_1,\dots,G_k\rangle=\mathcal A_n\bigr)=(1-2^{-k})^{n-1}.
\]
If \(n\to\infty\), \(k=k(n)\geq0\), and \(n2^{-k(n)}\to\lambda\in[0,\infty)\), then \(Z\) converges in distribution to \(\mathrm{Poisson}(\lambda)\) and the full-generation probability converges to \(e^{-\lambda}\). For every \(n\geq2\), the minimum number of generators is one; for \(n=1\), it is zero. The existence of a single generator for finite chains is classical and is not asserted to be independently novel.

## Assumptions and scope
All algebras use the finite full powerset, Boolean constants, and the indicated **reflexive forward** diamond. The underlying worlds are labelled and linearly ordered, and random subsets are independent and uniform. A modal subalgebra contains the Boolean constants and is closed under the diamond operation. The probability statement is not a statement about random accessibility relations, infinite frames, or nonuniform valuations. The depth parameter \(k\) may vary with \(n\) only as explicitly specified.

## Proof
**1. Consecutive runs are invariant.** Fix a generator tuple and let \(I_1,\ldots,I_r\) be the maximal runs of its common membership-word coloring, ordered from left to right. Each generator is a union of these intervals. Boolean operations preserve unions of runs. If \(X\) is a union of runs, either \(X\) is empty (and so is \(\Diamond X\)) or \(X\) has a rightmost point which is the last point of some run \(I_s\). Then \(\Diamond X=I_1\cup\cdots\cup I_s\), also a union of runs. Hence every term in the generated subalgebra is a union of runs.

**2. Runs are distinguishable by modal formulas.** Write \(a_s\in\{0,1\}^k\) for the color of \(I_s\). Adjacent colors are distinct. Let \(\delta_a\) be the Boolean conjunction asserting exactly the \(k\) memberships prescribed by \(a\), with the empty conjunction \(\top\) when \(k=0\). For each \(s\), define the nested modal formula
\[
\psi_s=\delta_{a_s}\wedge\Diamond(\delta_{a_{s+1}}\wedge\Diamond(\cdots\wedge\Diamond\delta_{a_r})),
\]
where \(\psi_r=\delta_{a_r}\). Every point of \(I_s\) satisfies \(\psi_s\), by choosing successive witnesses in the following runs. No point of a strictly later run \(I_t\), \(t>s\), can satisfy \(\psi_s\): a witnessing sequence requires \(r-s+1\) consecutive color tests, and, since adjacent tested colors differ, it visits at least \(r-s+1\) distinct runs; only \(r-t+1<r-s+1\) runs remain from \(I_t\) onward. Thus \(\psi_s\) separates run \(I_s\) from each later run. Every pair of distinct runs is therefore separated by an element of the generated Boolean algebra. Since this algebra is finite, its Boolean atoms are the individual runs. Consequently it contains every union of runs, completing the characterization.

**3. All subalgebras.** Any finite Boolean subalgebra \(\mathcal B\subseteq\mathcal P(C_n)\) has the atoms of a set partition of \(C_n\). Take those atoms as a finite tuple of modal-algebra generators for \(\mathcal B\); their membership words distinguish distinct partition cells. By step 2, the subalgebra they generate has as atoms the maximal consecutive runs of those words. Since \(\mathcal B\) is already closed under \(\Diamond\), it equals this generated algebra. Every partition atom must therefore be a consecutive interval. Conversely, step 1 shows that the unions of the intervals of any consecutive-block partition form a modal subalgebra. Such partitions are exactly the choices of the \(n-1\) boundaries at which to cut; algebra inclusion is inclusion of cut sets. The subalgebra lattice is therefore isomorphic to the Boolean lattice on those boundaries.

**4. Exact finite distribution.** There are \(m^n\) ordered generator tuples, identified with color words of length \(n\) over an alphabet of size \(m\). To obtain exactly \(r\) runs, choose \(r-1\) of the \(n-1\) possible change boundaries, choose the first color in \(m\) ways, and independently choose each following run color in \(m-1\) ways (different from the previous run). This proves the enumeration. Uniform independent generator subsets induce uniform independent color words at all worlds. Sequentially, after the first color, each new color equals its predecessor with probability \(1/m\), independent of all previous equality events: for any prescribed equality/difference pattern the number of word colorings is \(m(m-1)^d\) and its probability factors into Bernoulli factors. Hence \(Z\sim\mathrm{Bin}(n-1,1/m)\). A tuple generates the full algebra exactly when \(Z=0\), yielding the probability formula.

**5. Critical window and rank.** The binomial probability generating function is \((1+(z-1)/m)^{n-1}\). When \(n/m\to\lambda\) and \(n\to\infty\), it converges to \(\exp(\lambda(z-1))\), the probability generating function of \(\mathrm{Poisson}(\lambda)\). Taking \(z=0\) gives full-generation limit \(e^{-\lambda}\). For \(n\geq2\), a single alternating bit color has distinct adjacent values, hence generates all \(2^n\) subsets by step 2, while no generators produce the full algebra; for \(n=1\), Boolean constants already generate the two-element powerset. This also identifies the generic threshold \(2^k\) on the scale of \(n\).

## Verification
The independent constructive checker `checker.py` builds the Boolean color partition and repeatedly refines it by the genuine forward modal operation until it is stable. It compares the resulting number of atoms with the run count and the full histogram against the closed formula, exhaustively for \(1\leq n\leq6\) and \(0\leq k\leq2\). Separately, it enumerates all set partitions of up to seven worlds and directly checks closure under the diamond, verifying that exactly the consecutive interval partitions are stable. Running `python3 checker.py` produces `ALL_CHECKS_OK` and `ALL_PARTITION_CHECKS_OK`. These finite calculations corroborate but do not replace the general proof above.

## Relationship to prior work
Gabriel Agnew, *On Local Finiteness of Modal K4 Algebras* (arXiv:2606.02941v1, June 1, 2026) studies subalgebras of complex transitive-frame modal algebras through tuned partitions and establishes a general local-finiteness criterion. This supplies the mathematical motivation to quantify not only whether subalgebras are finite but their exact shape and generation multiplicity on a natural finite-chain family. The full available text (including Sections 2--3, the tuned-partition discussion and Theorem 3.16) was inspected; no exact chain subalgebra lattice, ordered-tuple distribution, or growing-generator Poisson statement was identified.

W. J. Blok, *The free closure algebra on finitely many generators* (Indagationes Mathematicae 39 (1977), 362--379; DOI 10.1016/1385-7258(77)90050-6) is a classical precursor to closure-algebra generation, and elementary one-generator phenomena should be attributed to this established context rather than claimed as new. Full-text access to this article was not obtained; priority uncertainty for an equivalent complete enumeration remains. The contribution assessed here is the **combined exact subalgebra-fiber law and stochastic threshold**, not the classical Boolean/algebraic definitions or mere existence of a single generator.

## Limitations
The classification exploits the linear, reflexive finite accessibility order; it is not asserted for arbitrary transitive frames. The exact distribution presupposes independently uniformly chosen generator subsets, not random formula syntax. The Poisson limit applies only to sequences satisfying its scaling hypothesis; discreteness of \(k\) can prevent an arbitrary full sequence from having a nonzero prescribed limit. The formulas and code do not establish priority over inaccessible historical sources, and no external independent audit has been performed.

## References
1. G. Agnew, *On Local Finiteness of Modal K4 Algebras*, arXiv:2606.02941v1, 2026-06-01. https://arxiv.org/html/2606.02941
2. W. J. Blok, *The free closure algebra on finitely many generators*, Indagationes Mathematicae 39 (1977), 362--379. https://doi.org/10.1016/1385-7258(77)90050-6
