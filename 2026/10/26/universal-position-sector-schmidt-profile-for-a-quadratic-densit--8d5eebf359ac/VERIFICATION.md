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

# Numerical verification and proof dependencies

To reproduce the finite checks, install dependencies from `requirements.txt` and run `python verify.py`. The script evaluates interlaced Airy and Airy-derivative zeros, solves the exact positive quartic for several positive couplings and resonances, and reconstructs the photon and atomic norms. For selected Airy states it Fourier-transforms the normalized momentum wavefunction, thereby calculating the dimensionless spatial first absolute and second moments, and compares characteristic functions against the expected uniform-orbit limit \(\sin(t)/t\). It reconstructs the reduced two-by-two Schmidt matrices and their positivity and determinants, and checks the positive joint-scaling crossover. The script completed 256 assertions successfully on the delivered source code.

The analytic reasoning, not these finite samples, proves the infinite-index results. Its critical lemma uses the oscillatory Airy asymptotic on compact subsets of the classically allowed momentum interval, explicit control of shrinking turning-point and central regions, disappearance of rapidly oscillating cross terms, and the resulting \(\sin(t)/t\) characteristic function. The exact virial second moment gives uniform integrability to pass from weak distribution convergence to \(\mathbb E|X|\to1/2\). The quartic equation and Airy-zero asymptotic then give the entire scaling profile. No separate external mathematical validation was conducted.

The numerical Fourier transform is performed on a finite periodic grid; its agreement for successively higher indices is corroboration, not an exhaustive estimate or a replacement for the Airy integral argument. The formal bipartition is \(L^2(\mathbb R)\otimes\mathbb C^2\) and is not a claim about a physical tensor factorization into photon and atomic many-body Hilbert spaces.
