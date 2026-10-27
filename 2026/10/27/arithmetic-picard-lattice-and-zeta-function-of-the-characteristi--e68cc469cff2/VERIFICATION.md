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

# Reproducibility of the arithmetic K3 calculation

The standalone `VERIFIER.py` enumerates all \(21\) points and all \(21\) dual lines in \(\mathbb P^2(\mathbb F_4)\), using \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\). It checks the full incidence array, constructs the symmetric \(42\)-generator intersection form and tests its rational rank \(22\).

The script does not mistake a rational full-rank minor for an integral basis. It uses exact rational coordinates followed by integer column Hermite normal form to obtain the image lattice of the full \(42\)-generator matrix; its determinant is \(-4\). It then expresses the Frobenius permutation in that **integral** lattice basis, checks its order two and trace eight, and uses tracked **unimodular** column operations to get a primitive basis of the fixed lattice. The fixed Gram matrix has determinant \(256\) and Smith invariant factors \(1^8,2^6,4\). The Hermite determinant of the \(28\) Frobenius orbit sums in the fixed basis is \(1\).

Independently, the smooth Mukai complete intersection in \(\mathbb P^2\times\mathbb P^2\), given by \(\sum_i x_i y_i^2=\sum_i x_i^2 y_i=0\), has \(21\) rational points over \(\mathbb F_2\) and \(105\) over \(\mathbb F_4\), verified by exhaustive enumeration. An exact check confirms that the formula \(1+q^2+q(15+7(-1)^n)\), \(q=2^n\), agrees for sample degrees with replacing each \(\mathbb F_q\)-rational \(A_1\) singular point of the purely inseparable plane model by its exceptional \(\mathbb P^1\).

The geometric facts that the \(21\) singularities are ordinary \(A_1\) points and the \(42\) curves generate all of \(\operatorname{NS}\) integrally are **published inputs**, specifically Dolgachev–Kondō (2003), Sections 3.3 and 4.2. The verification script checks the arithmetic linear algebra using those inputs; it does not derive these nontrivial geometric facts from finite enumeration alone. No third-party verification or independent scientific audit is asserted.
