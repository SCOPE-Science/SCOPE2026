# Seven rank-three theories of prime cyclic groups

## Finding

Write \(C_p=(\mathbb Z/p\mathbb Z;0,R)\), where \(p\) is prime and \(R(u,v,w)\) holds precisely when \(u+v=w\). The language has equality, the named zero, and the **ternary addition relation** rather than a binary addition function. Let \(\equiv_3\) mean agreement on all first-order sentences of quantifier rank at most three, with no bound on the total number of quantifiers or variables.

**Theorem.** For any primes \(p,q\),
\[
C_p\equiv_3 C_q
\quad\Longleftrightarrow\quad
\bigl(p=q\le13\bigr)\ \lor\ \bigl(p\ge17\text{ and }q\ge17\bigr).
\]
Thus the prime-cyclic family has **exactly seven rank-three theories**, represented by the groups of orders \(2,3,5,7,11,13,17\). Every member is rank-three equivalent to a member of order at most \(17\), and \(17\) is the sharp largest minimum representative order within this family.

An explicit sentence of rank three holds in \(C_{11}\) and in no other prime-order group:
\[
\begin{split}
\Phi_{11}:=\exists x\,\exists y\,[x\ne0&\land
(\exists z\,[R(x,x,z)\land R(x,z,y)])\\
&\land(\exists w\,[R(y,y,w)\land R(w,w,x)])].
\end{split}
\]
This short formula also gives a concrete counterexample to the specialized four-round lower bound for prime orders \(11\) and \(13\) stated in the archival literature described below.

## Assumptions and scope

The underlying structure is the additive group of a **prime** field, presented relationally. The statement is not about a language with a binary function symbol for addition; replacing \(R\) with a function symbol changes which term equations count as atomic and hence changes quantifier rank. It neither classifies composite-order cyclic groups at rank three nor addresses ranks greater than three. First-order formulas may reuse variables and may contain conjunctions of branches with distinct bound variables; quantifier rank counts maximal nesting depth, not total quantified occurrences.

## Proof

**1. The exact finite-depth invariant.** For a selected tuple \(\bar a\), let \(\mathrm{At}_p(\bar a)\) be its complete atomic diagram: the truth values of all equalities and all expressions \(R(s_i,s_j,s_k)\), where each \(s_i\) is a selected coordinate or the named zero. Define recursively
\[
T_{0,p}(\bar a)=\mathrm{At}_p(\bar a),\qquad
T_{r+1,p}(\bar a)=\bigl(\mathrm{At}_p(\bar a),
\{T_{r,p}(\bar a,b):b\in C_p\}\bigr).
\]
The standard induction on first-order formulas (equivalently, the ordinary Ehrenfeucht--Fraïssé game) gives
\[
C_p\equiv_3 C_q\iff T_{3,p}(())=T_{3,q}(()).
\]
Multiplication by any nonzero residue is an automorphism of this additive relational structure. Consequently the first move has only two automorphism orbits, represented by \(0\) and \(1\).

**2. The twelve atomic third-move candidates.** Fix \(x\ne0\) and an arbitrary \(y\). In odd prime characteristic, the nontrivial atomic addition equations involving a third selected variable \(z\) force it to be one of exactly twelve values. Use the following twelve atomic predicates (the labels are merely abbreviations):

| Predicate | Atomic equation | Forced value of \(z\) |
|---|---|---|
| \(E_0\) | \(R(z,x,0)\) | \(-x\) |
| \(E_1\) | \(R(z,x,y)\) | \(y-x\) |
| \(E_2\) | \(R(z,y,0)\) | \(-y\) |
| \(E_3\) | \(R(0,0,z)\) | \(0\) |
| \(E_4\) | \(R(z,z,y)\) | \(y/2\) |
| \(E_5\) | \(R(0,y,z)\) | \(y\) |
| \(E_6\) | \(R(y,y,z)\) | \(2y\) |
| \(E_7\) | \(R(z,z,x)\) | \(x/2\) |
| \(E_8\) | \(R(z,y,x)\) | \(x-y\) |
| \(E_9\) | \(R(0,x,z)\) | \(x\) |
| \(E_{10}\) | \(R(x,y,z)\) | \(x+y\) |
| \(E_{11}\) | \(R(x,x,z)\) | \(2x\) |

This table is exhaustive: every atomic relation on \(0,x,y,z\) that involves \(z\) can, after permuting summands, be written in one of these forms, is a tautology, or reduces by cancellation to an equation involving only the previously chosen parameters; equality with \(z\) is included because \(R(0,u,z)\) expresses \(u=z\). The atomic equations not involving \(z\) are determined solely by \((x,y)\). A value of \(z\) outside all twelve positions realizes the remaining generic atomic extension type.

Normalize \(x=1\) and put \(t=y/x\). A pair of **distinct** candidate affine functions of \(x,y\) coincides if and only if \(t\) belongs to the following set of thirteen rational exceptional ratios, interpreted modulo \(p\):
\[
S=\left\{-2,-1,-\frac12,0,\frac14,\frac13,\frac12,
\frac23,1,\frac32,2,3,4\right\}.
\]
To obtain this list, write the twelve functions as \(\alpha_i x+\beta_i y\), with coefficients read directly from the table, and solve each of the \(\binom{12}{2}\) equations
\[
(\alpha_i-\alpha_j)+(\beta_i-\beta_j)t=0.
\]
Pairs having equal \(\beta\)-coefficients but different \(\alpha\)-coefficients never coincide in characteristic at least \(17\). In all other pairs, the finite list of solutions is exactly \(S\). The denominators of members of \(S\) are at most four. Moreover, for distinct \(u,v\in S\), the integer
\[
\bigl|\operatorname{num}(u)\operatorname{den}(v)
-\operatorname{num}(v)\operatorname{den}(u)\bigr|
\]
is between \(1\) and \(15\); therefore the thirteen ratios remain distinct modulo every prime \(p\ge17\). All relations among the twelve candidate values are consequently the same for corresponding exceptional ratios in every such prime field. At a ratio not in \(S\), all twelve candidates are distinct.

The atomic pair diagram of \((1,t)\) can change only at \(t=0,1,-1,2,1/2\), a subset of \(S\). For \(p\ge17\), at least one \(z\) avoids all twelve candidates, and each of the thirteen exceptional ratios as well as at least one nonexceptional ratio occurs. It follows that the collection of one-move extension types \(T_{1,p}(1,t)\), with \(t\) varying, is independent of the prime \(p\ge17\): for each \(s\in S\) there is one fixed type, and nonexceptional ratios have one fixed additional type.

If the first chosen element is zero, the second choice is either zero or nonzero; all nonzero choices are conjugate under scaling. Their third-move atomic possibilities likewise depend only on finitely many residues \(0,\pm1,2,1/2\), with a generic residue remaining for \(p\ge17\). Thus \(T_{2,p}(0)\) is also independent of \(p\ge17\). Together these observations show that \(T_{2,p}(1)\), \(T_{2,p}(0)\), and finally \(T_{3,p}(())\) are common to every prime \(p\ge17\). This proves the infinite equivalence assertion, without extrapolation from finite tests.

**3. Six explicit separations.** In the language \(R\), let
\[
\begin{aligned}
\Phi_2 &:=\exists x\,[x\ne0\land R(x,x,0)],\\
\Phi_3 &:=\exists x\exists y\,[x\ne0\land R(x,x,y)\land R(x,y,0)],\\
\Phi_5 &:=\exists x\exists y\exists z\,[x\ne0\land R(x,x,y)\land R(y,y,z)\land R(x,z,0)],\\
\Phi_7 &:=\exists x\exists y\exists z\,[x\ne0\land R(x,x,y)\land R(y,y,z)\land R(z,z,x)].
\end{aligned}
\]
Each \(\Phi_j\) is true in a prime-order group exactly when the prime is \(j\). The two independent inner branches of \(\Phi_{11}\), displayed above, impose \(y=3x\) and \(4y=x\), so \(11x=0\) with \(x\ne0\). Hence \(\Phi_{11}\) isolates prime \(11\), and its quantifier rank is three despite having four quantified variable occurrences.

The final separation uses the table of atomic predicates. Define the rank-three sentence
\[
\Gamma:=\exists x\exists y\left[
 x\ne0\ \land\!
 \bigwedge_{0\le i<j\le11}
 \neg\exists z\,\bigl(E_i(x,y,z)\land E_j(x,y,z)\bigr)
 \right].
\]
For odd primes at most \(11\), the twelve forced values of \(z\) lie in a set of at most eleven residues, so two must coincide. For prime \(2\), the direct equations \(z=0\) and \(z=2x\) coincide, so \(\Gamma\) is also false. At prime \(13\), the thirteen rational ratios in \(S\) give all thirteen residues: their images, in displayed order, are
\[
11,12,6,0,10,9,7,5,1,8,2,3,4.
\]
Consequently \(\Gamma\) remains false. At every prime \(p\ge17\), choose \(x=1\) and \(y=t\) outside \(S\); then no pair of forced values coincides, so \(\Gamma\) is true. Its quantifier rank is precisely three.

The five characteristic-isolating sentences distinguish \(2,3,5,7,11\) from every other prime. The sentence \(\Gamma\) distinguishes the \(p\ge17\) class from the remaining prime \(13\). Hence exactly seven classes occur, and the largest least prime-order representative is \(17\). This completes the proof.

## Verification

Run `python3 verify.py` in the directory containing the standalone verifier; its `verify.log` records the output. The verifier constructs the twelve affine candidates, enumerates all pairwise coincidences using exact rational arithmetic, verifies the thirteen-ratio list and the numerator bound \(15\), checks the separating formulas and generic threshold in small prime fields, and independently computes full recursive atomic-extension invariants in the prime fields of orders \(2,3,5,7,11,13,17,19,23\). It reproduces seven distinct signatures, with the three tested primes at least seventeen agreeing. The infinite result is supported by the preceding symbolic proof, not by the finite signature tests.

## Relationship to prior work

Walid Gomaa's 2007 dissertation, *Model Theory and Complexity Theory*, Chapter 3, Sections 3.3--3.4, studies the same ternary-relational group language and the prime-order cyclic groups. Its Theorem 3.3 gives a purported lower bound of \(n+1\) game rounds when \(2^n<p<2^{n+1}\) and \(p<q\). The journal paper *Descriptive Complexity of Finite Abelian Groups* (2010), Section 4, Theorem 4.4 and Corollary 4.5, state the corresponding lower bound. For \(p=11\), \(q=13\), this specializes to at least four rounds. The explicit \(\Phi_{11}\) above has rank three and holds in \(C_{11}\), not \(C_{13}\); therefore that numerical lower-bound assertion **does not hold as stated in this instance**. This observation does not purport to invalidate unrelated asymptotic estimates or other theorems of those works.

Other work on addition-chain and signed-binary constructions gives upper bounds for distinguishing prime cyclic groups, but does not state the complete seven-class rank-three equivalence relation established here. The exact threshold and the simple rank-three separator are the differences in statement and implication, not merely a difference of notation.

## Limitations

The assertion concerns only prime cyclic groups under relational addition and only quantifier rank three. The source comparison was not a complete survey of every unpublished or unindexed treatment; further independent literature review may find an equivalent classification. The comparison with the earlier published lower bound is a statement-level mathematical incompatibility, with a directly evaluable counterexample, not an external retraction or independent peer review. The checks presented here are not independent; no independent audit is claimed.

## References

1. W. Gomaa, *Model Theory and Complexity Theory*, PhD thesis, University of Maryland, 2007, Chapter 3, Section 3.4; publicly deposited 2007-07-06. Repository identifier: `https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440`.
2. W. Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation **20** (2010), 1087--1116. DOI `10.1142/S0218196710006047`; especially Section 4, Theorem 4.4 and Corollary 4.5.
3. L. Libkin, *Elements of Finite Model Theory*, Springer, 2004 (standard finite-depth Ehrenfeucht--Fraïssé characterization).
