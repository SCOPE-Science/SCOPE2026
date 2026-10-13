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

The proof in `RESULT.md` is universal. The computation below is corroborative and checks every finite certificate used in the argument.

The attached `verify.py` first sieves through the finite cutoff in Defant's proof of the consecutive-prime ratio lemma and verifies that the only finite indices violating
\[
p_{j+1}^2<2p_j^2
\]
are
\[
j=1,\quad j=2,\quad j=4.
\]

It then checks exactly that
\[
\frac{50}{49}
<
\frac{122}{121}\frac{170}{169}\frac{290}{289}\frac{362}{361}
=
\frac{128075600}{125495513},
\]
which is the only exceptional tail inequality needed for the squarefree \(r=2\) proof.

The interval separation uses
\[
\zeta(2)>
1+\frac14+\frac19+\frac1{16}+\frac1{25}+\frac16
=
\frac{5869}{3600},
\]
where the final \(1/6\) is the elementary integral lower bound for the tail from \(6\) onward. Hence
\[
\pi^2=6\zeta(2)>\frac{5869}{600}>\frac{243}{25}.
\]
The checker verifies all rational comparisons and the endpoint identities.

Finally, it enumerates a finite range of squarefree integers and confirms that every directly computed \(\sigma_{-2}\) value lies in the claimed union. This enumeration does not prove the closure theorem; it only stress-tests the formulas.
