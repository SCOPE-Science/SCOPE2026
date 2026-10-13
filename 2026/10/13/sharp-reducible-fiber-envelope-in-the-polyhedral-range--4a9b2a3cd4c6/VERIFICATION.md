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

The initiating primary abstract was checked for the precise setup and definitions:
\[
\delta(\pi)=\sum_i\frac{\lfloor n_i^2/4\rfloor}{n_i},
\qquad
N(\pi)=\sum_i n_i,
\]
with \(\chi=\chi(\mathcal O_X)\ge3\), finite Mordell--Weil group, and reducible semistable fibers \(I_{n_i}\). It states that \(\delta(\pi)\le\chi\) is the rational-polyhedral Mori-cone range and records the example
\[
I_4+3I_3+23I_1
\]
at \(\chi=3\).

For each integer \(n\ge2\), set
\[
d(n)=\frac{\lfloor n^2/4\rfloor}{n}.
\]
If \(n\) is even, then
\[
d(n)-\frac{2n}{9}=\frac n{36}>0.
\]
If \(n\) is odd, then
\[
d(n)-\frac{2n}{9}
=
\frac{n^2-9}{36n}\ge0,
\]
with equality exactly at \(n=3\). Hence
\[
\delta(\pi)\ge\frac{2N(\pi)}9
\]
for every finite reducible-fiber list, which proves
\[
N(\pi)\le\left\lfloor\frac{9\chi}{2}\right\rfloor.
\]

For odd \(\chi\) at the integer maximum, the total defect is at most \(1/9\). The exact small defects are
\[
e(2)=\frac1{18},
\qquad
e(3)=0,
\qquad
e(4)=\frac19,
\qquad
e(5)=\frac4{45}.
\]
All remaining sizes have defect greater than \(1/9\). Since the target total is congruent to \(1\) modulo \(3\), the only permitted non-\(3\) contributions are \(4\) or \(2+2\), giving the two stated patterns.

A finite exact-rational enumeration for \(3\le\chi\le8\) returned precisely:
\[
\chi=3:\quad 2I_2+3I_3,\ I_4+3I_3;
\]
\[
\chi=4:\quad 6I_3;
\]
\[
\chi=5:\quad 2I_2+6I_3,\ I_4+6I_3;
\]
and the same parity pattern thereafter. This was only a sanity check; the displayed proof is uniform in \(\chi\).

For the source's \(\chi=3\) example,
\[
\delta(\pi)=1+3\cdot\frac23=3,
\qquad
N(\pi)=4+3\cdot3=13,
\]
so the example attains the bound.

The full primary PDF of the initiating preprint was not available through the accessible public full-text route during verification. This limits originality inspection, not correctness of the theorem, because all premises used in the proof are stated in the primary abstract. No claim is made that every numerically extremal multiset is geometrically realized.
