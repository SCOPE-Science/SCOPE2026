---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

Let \(x,y\) be the Chern roots of \(\mathcal S^\vee\) and \(H=x+y\). The two quadric equations define the fourfold as the regular zero locus of
\[
E=\bigl(\operatorname{Sym}^2\mathcal S^\vee\bigr)^{\oplus2}
\]
inside \(\operatorname{Gr}(2,7)\).

The roots of one symmetric-square summand are
\[
2x,\quad x+y,\quad 2y.
\]
Using
\[
[T_G]=7[\mathcal S^\vee]-[\mathcal S^\vee\otimes\mathcal S]
\]
and subtracting the normal bundle gives
\[
c_1(T_F)=H
\]
and
\[
\operatorname{ch}_2(T_F)=-\frac52(x^2+y^2).
\]

The zero-locus class is
\[
[F]=c_6(E)=16x^2y^2H^2.
\]
For \(\operatorname{Gr}(2,7)\), integration of a symmetric degree-\(10\) polynomial is the coefficient
\[
[x^6y^5](x-y)f(x,y).
\]
Therefore
\[
\operatorname{ch}_2(T_F)\cdot H^2=-40
\]
and
\[
H^4=80.
\]

The bundled script `verify_ch2.py` independently replays these two coefficient extractions using exact rational arithmetic and terminates with `VERIFY_OK`.

The recent source was checked in full for smoothness, projectivity, and its explicit \(g=3\) motivic class. The definition of weakly \(2\)-Fano and the scope of the high-index classification were independently checked in the standard \(2\)-Fano reference. The general tautological symmetric-power and Grassmannian coefficient machinery was checked in the full Fano-scheme reference.

No finite experiment substitutes for a proof: the script verifies arithmetic in a symbolic identity already established in the proof.
