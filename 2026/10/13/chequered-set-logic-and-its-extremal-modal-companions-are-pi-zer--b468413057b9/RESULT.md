# Chequered-set logic and its extremal modal companions are Pi-zero-one complete
## Finding

Fix an effective G\"odel coding of propositional formulas. Then
\[
\mathsf{Cheq},\qquad
\mathsf{S4.FPFA}=\tau(\mathsf{Cheq}),\qquad
\mathsf{L}_{\infty}=\sigma(\mathsf{Cheq})
\]
are all \(\Pi^0_1\)-complete under computable many-one reductions.

Equivalently, the nonvalid formulas of each of these three logics form a recursively enumerable complete set.

The lower bound for \(\mathsf{Cheq}\) is supplied by the recent reduction from Medvedev logic. The upper bound is supplied by its effective finite-frame semantics. The same exact complexity then transfers to both extremal modal companions through the G\"odel translation and their effective finite-frame characterizations.

## Assumptions and scope

The intermediate logic \(\mathsf{Cheq}\) is characterized by the finite partial-function frames
\[
\mathbf A_n\cong\mathbf V_n,
\qquad n\ge1,
\]
where \(\mathbf V_n\) is the \(n\)-fold product of the two-fork.

The greatest modal companion is
\[
\mathsf{L}_{\infty}=\sigma(\mathsf{Cheq})
=
\mathsf{ML}(\{\mathbf A_n:n\ge1\}),
\]
and the least modal companion is
\[
\mathsf{S4.FPFA}=\tau(\mathsf{Cheq})
=
\mathsf{ML}(\{\mathbf A_n:n\ge1\}^{\bullet}),
\]
where \(\mathcal C^{\bullet}\) denotes the finite thickenings of the finite posets in \(\mathcal C\).

Completeness is with respect to computable many-one reductions between G\"odel codes of formulas.

## Proof

### The intermediate logic

Pawlowski proves that Medvedev logic \(\mathsf{Med}\) is \(\Pi^0_1\)-complete under computable many-one reductions.

Xiao defines, for each intuitionistic formula \(\varphi\), two fresh variables \(p,q\),
\[
\psi_0=p\vee\neg p,
\qquad
\psi_1=\neg p\vee\neg q,
\]
and the formula
\[
C(\varphi)
=
\bigl((\varphi^{\psi_0}\to\psi_1)\to\psi_1\bigr),
\]
where \(\varphi^{\psi_0}\) is the Friedman translation.

Xiao's Theorem 6.1 proves
\[
\varphi\in\mathsf{Med}
\quad\Longleftrightarrow\quad
C(\varphi)\in\mathsf{Cheq}.
\]
Choosing the two least variables absent from \(\varphi\) makes \(C\) an effective syntactic transformation. Hence \(\mathsf{Cheq}\) is \(\Pi^0_1\)-hard.

It remains to prove the matching upper bound. For a fixed input formula \(\theta\), enumerate
\[
n=1,2,3,\ldots.
\]
For each finite frame \(\mathbf V_n\), enumerate all persistent valuations of the finitely many variables occurring in \(\theta\), and evaluate \(\theta\) at every world. All of these searches are finite at fixed \(n\), and the frame \(\mathbf V_n\) is computable uniformly from \(n\).

If \(\theta\notin\mathsf{Cheq}\), some finite \(\mathbf V_n\), valuation, and world refute it, so this enumeration eventually finds a witness. Therefore the complement of \(\mathsf{Cheq}\) is recursively enumerable, equivalently
\[
\mathsf{Cheq}\in\Pi^0_1.
\]
Together with hardness,
\[
\mathsf{Cheq}
\text{ is }\Pi^0_1\text{-complete}.
\]

### The greatest modal companion

By definition of modal companion, the computable G\"odel translation \(T\) satisfies
\[
\varphi\in\mathsf{Cheq}
\quad\Longleftrightarrow\quad
T(\varphi)\in\mathsf{L}_{\infty}.
\]
Thus \(\mathsf{L}_{\infty}\) is \(\Pi^0_1\)-hard.

Xiao records the finite-frame characterization
\[
\mathsf{L}_{\infty}
=
\mathsf{ML}(\{\mathbf A_n:n\ge1\}).
\]
The frames \(\mathbf A_n\) are uniformly finite and computable. A modal nonvalidity witness is therefore found by enumerating \(n\), valuations of the input variables on \(\mathbf A_n\), and worlds. Hence
\[
\mathsf{L}_{\infty}\in\Pi^0_1.
\]
So \(\mathsf{L}_{\infty}\) is \(\Pi^0_1\)-complete.

### The least modal companion

Again the modal-companion definition gives
\[
\varphi\in\mathsf{Cheq}
\quad\Longleftrightarrow\quad
T(\varphi)\in\mathsf{S4.FPFA},
\]
so \(\mathsf{S4.FPFA}\) is \(\Pi^0_1\)-hard.

By the finite-thickening characterization,
\[
\mathsf{S4.FPFA}
=
\mathsf{ML}(\{\mathbf A_n:n\ge1\}^{\bullet}).
\]
This frame class is effectively enumerable. One can enumerate finite preorders and retain exactly those whose quotient by mutual accessibility is isomorphic to some \(\mathbf A_n\); all checks are finite and decidable. For every retained finite preorder, enumerate all valuations of the finitely many input variables and all worlds. Thus modal nonvalidity is recursively enumerable, and
\[
\mathsf{S4.FPFA}\in\Pi^0_1.
\]
Therefore \(\mathsf{S4.FPFA}\) is \(\Pi^0_1\)-complete.

## Verification

The proof uses four source-level facts that were checked directly.

First, Pawlowski states and proves that \(\mathsf{Med}\) is \(\Pi^0_1\)-complete under computable many-one reductions, with the upper bound obtained from finite countermodels.

Second, Xiao's Theorem 6.1 gives the exact biconditional
\[
\varphi\in\mathsf{Med}
\quad\Longleftrightarrow\quad
C(\varphi)\in\mathsf{Cheq}.
\]

Third, Xiao defines \(\mathsf{Cheq}\) by the uniformly finite frames \(\mathbf V_n\cong\mathbf A_n\), which makes its complement recursively enumerable.

Fourth, Xiao records \(\mathsf{L}_{\infty}\) and \(\mathsf{S4.FPFA}\) as the greatest and least modal companions of \(\mathsf{Cheq}\), together with the finite-frame and finite-thickening characterizations needed for their \(\Pi^0_1\) upper bounds.

No finite experiment is used as evidence for an infinite statement. The upper-bound algorithms are exhaustive semidecision procedures whose termination is claimed only on nonvalid inputs.

## Relationship to prior work

Pawlowski determines the exact arithmetical complexity of Medvedev logic. Xiao subsequently gives a computable membership-preserving reduction from Medvedev logic to \(\mathsf{Cheq}\), but states the consequence only as undecidability. Xiao's paper also places \(\mathsf{Cheq}\) between its least and greatest modal companions and gives the relevant finite-frame semantics.

The present observation combines those ingredients to sharpen undecidability to \(\Pi^0_1\)-completeness and propagates that exact classification to both extremal modal companions.

Targeted searches for \(\Pi^0_1\)-completeness of \(\mathsf{Cheq}\), \(\mathsf{S4.FPFA}\), and \(\mathsf{L}_{\infty}\), including searches under the phrases “logic of chequered sets,” “co-recursively enumerable,” and “arithmetical complexity,” did not locate a prior statement of this three-logic classification.

## Limitations

The result classifies the arithmetical complexity of validity, not finer resource-bounded complexity on restricted fragments.

The proof depends on the correctness of the two recent primary results: Pawlowski's \(\Pi^0_1\)-completeness theorem for Medvedev logic and Xiao's exact reduction theorem.

No claim is made that arbitrary modal companions of arbitrary \(\Pi^0_1\)-complete intermediate logics must themselves have recursively enumerable complements; here the upper bounds use the explicit effective finite-frame characterizations.

## References

[1] Han Xiao, “Non-finite Axiomatizability and Undecidability of \(\mathsf{Cheq}\),” arXiv:2609.39577v1, first posted 30 September 2026.

[2] Pawel Pawlowski, “Medvedev Logic is Not Decidable. It is \(\Pi^0_1\)-Complete. Who Would Have Guessed?,” arXiv:2609.11576v1, first posted 10 September 2026.
