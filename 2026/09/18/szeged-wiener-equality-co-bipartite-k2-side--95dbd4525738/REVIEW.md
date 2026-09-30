# Review

**Same-model correctness review: retained. Independent audit on 29 September 2026:
correctness passed; originality/provenance repaired.**

## Correctness

The exact formula
\[
\eta(G)=8ab+2c(a+b)+3d(a+b)+4cd-4d
\]
is correct. It follows directly from the diameter-two distance identity
\[
n_{uv}(u)=\deg(u)-|N(u)\cap N(v)|
\]
applied to the four cross-neighborhood types and to the edges incident with the
two-vertex clique side. The equality equation is
\[
8ab+2c(s-1)+d(3s+4c-6)-2s-4=0,\qquad s=a+b,
\]
and its nonnegative integer solutions with \(q\ge8\) are exactly the stated infinite
family plus the single \(q=8\) exceptional isomorphism type.

The bundled standard-library verifier independently constructs the graphs and checks
the defining Szeged and Wiener sums on 10,165 two-connected parameter quadruples for
\(q\le20\). This supports, but is not needed for, the general proof.

## Originality and provenance correction

The original review's statement that this was an independently original subclass
classification is withdrawn. Repository history shows that the broader SCOPE record

`2026/09/18/szeged-wiener-equality-clique-n-minus-two--a84aa8e708f8`

was committed at 2026-09-18 03:47:31 UTC, while this record was committed at
2026-09-18 16:45:35 UTC. The earlier record already contains the adjacent-\(x,y\)
formula and the same equality classification, with its symbols \(C,D\) interchanged.
Under \(C_{\rm earlier}=d\) and \(D_{\rm earlier}=c\), its formula becomes the formula
in this record exactly.

Accordingly this record is retained as an alternate derivation and reproducibility
package for a specialization of the earlier broader result. No separate discovery
priority is claimed.

## Scientific value

The record remains useful as a focused, transparent derivation and as an exhaustive
small-parameter verification package. Its value is corroborative and reproducibility-
oriented rather than a distinct advance beyond the earlier broader SCOPE theorem.

## Limitations

- The global Zhang–Li equality problem remains open.
- The theorem treats only the co-bipartite subclass with a two-vertex clique side.
- The corrected record makes no separate originality claim relative to the earlier
  same-day SCOPE theorem.
