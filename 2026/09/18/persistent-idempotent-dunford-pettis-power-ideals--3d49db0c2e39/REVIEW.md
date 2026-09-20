# Same-model review

## Claim reviewed

For \(X=L^1[0,1]\), let \(\mathcal D=\operatorname{DP}(X)\),
\(\mathcal G=\mathcal G_{\ell^1}(X)\), and
\[
\mathcal I_n=\overline{\operatorname{span}}
\{T_1\cdots T_n:T_i\in\mathcal D\}.
\]
The record claims that there is a projection
\(P\in\mathcal D\setminus\mathcal G\) lying in every \(\mathcal I_n\);
that every \(\mathcal I_n\), \(n\ge2\), is a proper large closed ideal
strictly above \(\mathcal G\); and that the quotient
\(D=\mathcal D/\mathcal G\) has a nonzero idempotent in
\(\bigcap_n D^{[n]}\).

## Correctness review

**Passed.**

Acuaviva's Theorem A explicitly supplies a Dunford–Pettis projection on
\(L^1[0,1]\) whose range has the Schur property and fails the Radon–Nikodým
property. The complex case is treated in the same paper.

Nasseri explicitly identifies the representable ideal \(\mathcal G\) on
\(L^1[0,1]\) with the operators factoring through \(\ell^1\).

If \(P=BA\) factored through \(\ell^1\), then on \(Y=P(X)\) one has
\(BAy=y\). Therefore \(A|_Y\) is bounded below and embeds \(Y\) isomorphically
as a closed subspace of \(\ell^1\). Since \(\ell^1\) has the
Radon–Nikodým property and the property is inherited by closed subspaces,
this contradicts Acuaviva's non-RNP conclusion. Hence \(P\notin\mathcal G\).

All remaining algebraic steps were checked directly:

- \(P^n=P\), so \(P\in\mathcal I_n\) for all \(n\).
- If \(G=AB\) factors through \(\ell^1\), and
  \(U:\ell^1\to X\), \(V:X\to\ell^1\) satisfy \(VU=I_{\ell^1}\), then
  \(G=(AV)(UV)^{n-2}(UB)\), proving \(\mathcal G\subseteq\mathcal I_n\).
- For \(n\ge2\), \(\mathcal I_n\subseteq\mathcal I_2\).
- Nasseri proves \(\mathcal I_2\subsetneq\mathcal D\).
- \(P\) is not strictly singular because it is the identity on its
  infinite-dimensional range.
- Every \(APB\) factors as
  \((AP)P^{n-2}(PB)\), with all factors Dunford–Pettis, giving a common
  large ideal in all powers.
- Modulo \(\mathcal G\), \(e=P+\mathcal G\) is a nonzero idempotent and hence
  belongs to every closed power.

No hidden complementability assertion is used: the range of \(P\) is
complemented by definition because \(P\) is a projection.

## Originality review

**Passed, to the best of our knowledge.**

The key source papers are extremely recent and were checked at theorem level.

Acuaviva's preprint states Theorem A: a Dunford–Pettis projection with Schur
range failing the Radon–Nikodým property. It does not mention Nasseri's power
ideals.

Nasseri's preprint defines \(D=\mathcal D/\mathcal G\), proves
\(0\ne D^{[2]}\subsetneq D\), and in its Further Questions section states that
its construction shows \(D^{[n]}\ne0\) for every \(n\) using convolution
powers, while leaving strict decrease beyond the first inclusion open. It
cites Acuaviva in connection with a separate announced construction of many
closed ideals, but does not state that Acuaviva's projection yields a common
nonzero idempotent in all powers or a common proper large ideal.

Targeted searches using combinations of the terms “Dunford-Pettis
projection”, “representable operator”, “factor through l1”, “idempotent”,
“power ideal”, “Radon-Nikodym”, and “Jacobson radical” did not locate the
same conclusion. The current SCOPE repository was also searched by the main
objects and source names; no overlapping record was found.

The general factorization/RNP ingredients are classical and are not claimed
as new. In particular, Lewis–Stegall underlies the identification of
representable operators with \(\ell^1\)-factorable operators on \(L^1\).

### Residual literature risk

Elias Saab's 1982 paper *On Dunford-Pettis Operators* is closely related:
its accessible abstract connects complemented subspaces, Dunford–Pettis
operators, representability, and the Radon–Nikodým property. The full article
was not inspected in this review. It may contain a general lemma subsuming
part of the short argument that a representable projection has RNP-type
range. It cannot contain the specific 2026 synthesis with Acuaviva's newly
constructed projection and Nasseri's newly defined power chain, which is the
originality claim made here.

The result is not claimed to settle whether the power ideals are pairwise
distinct.

## Value review

**Passed.**

Nasseri's current evidence for \(D^{[n]}\ne0\) uses a different convolution
power at each order. The present observation shows a substantially stronger
persistence phenomenon: one nonzero idempotent survives every power, and the
entire closed ideal it generates survives every power. Thus any eventual
strictly decreasing power chain has a nonzero common core.

At the operator level, every \(\mathcal I_n\), \(n\ge2\), is immediately a
proper large closed ideal, not merely a nonzero power. The quotient
\(D=\mathcal D/\mathcal G\) is also shown to be nonradical.

## Sources inspected

- Antonio Acuaviva, arXiv:2609.17283v1, full accessible arXiv text including
  Theorem A and the proof of the Schur/non-RNP properties:
  https://arxiv.org/abs/2609.17283
- Amir Bahman Nasseri, arXiv:2609.18348v1, full accessible arXiv text,
  especially Sections 1, 5, 7 and 8:
  https://arxiv.org/abs/2609.18348
- Lewis–Stegall bibliographic/abstract record:
  https://doi.org/10.1016/0022-1236(73)90022-0
- Elias Saab, bibliographic record and abstract:
  https://doi.org/10.4153/CMB-1982-028-8

Same-model review: passed. Independent audit: not yet performed.
