# Independent audit — 2026-10-01

## Outcome

**Passed.** The final scientific claim in `RESULT.md` survives correctness, originality, and value review without modification.

## Correctness

Using \(\psi(G)=t h+(A-t)c\) for P cyclic normal, ψ-divisibility for H gives \(h\mid(A-t)c\), while ψ-divisibility for PC=P×C gives \(Ac\mid t(h-c)\). Writing \(h=dx,\ c=dy\) with \((x,y)=1\) yields \(x\mid A-t\) and \(Ay\mid t(x-y)\). Since \(\gcd(A,t)=1\) for a cyclic p-group, \(A\mid(x-y)\), contradicting \(0<x-y<x\le A-t<A\). Schur--Zassenhaus gives the normal-Sylow corollary. In a nonnilpotent Z-group the standard ZM presentation supplies a noncentral normal cyclic Sylow subgroup, so it is excluded; the remaining nilpotent Z-groups are cyclic and the 2014 abelian theorem gives square-free order.

## Originality

The 2020/2021 Lazorec paper explicitly leaves the nonnilpotent square-free-order case open after a restricted ZM obstruction, while the 2014 abelian classification covers only abelian groups. The submitted normal-cyclic-Sylow theorem directly resolves the open Z-group/square-free slice and is not implied by the inspected sources.

The four structured comparisons are recorded in the companion JSON file. The closest primary source is Lazorec's 2021 paper, whose normal-cyclic-Sylow formula is used as an ingredient but whose restricted ZM result leaves the square-free nonnilpotent case open. Harrington--Jones--Lamarche supplies the abelian classification only.

## Value

The theorem gives a broad structural obstruction, classifies all ψ-divisible Z-groups, and resolves a published square-free-order open problem theoretically rather than by extending a finite computation. This is a clearly motivated and reusable finite-group result.

## Sources inspected

- M.-S. Lazorec, *On a Divisibility Property Involving the Sum of Element Orders*, DOI 10.1007/s40840-020-00987-8. Full relevant text inspected, including Lemma 2.1(iii), Proposition 2.4, and the square-free-order open problem.
- J. Harrington, L. Jones, A. Lamarche, *Characterizing Finite Groups Using the Sum of the Orders of the Elements*, DOI 10.1155/2014/835125. Relevant full text inspected, including the abelian classification.

## Limitations and risk

The theorem does not classify all finite ψ-divisible groups. Originality is to the best of current searches; an unindexed equivalent observation could still exist.
