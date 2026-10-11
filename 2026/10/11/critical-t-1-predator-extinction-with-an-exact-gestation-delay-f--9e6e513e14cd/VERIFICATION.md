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
# Verification of the critical extinction theorem

The complete equations and exact hypotheses appear in `RESULT.md`. Scientific verification performed:

1. Reconstructed the nonnegative solution bounds without assuming the source's boundedness proof: prey logistic upper comparison, intermediate predator forced linear upper bound, top predator forced linear upper bound.
2. Directly differentiated the critical mass \(P(t)=y(t)+d\int_{t-\tau_1}^t y(s)\,ds\) and checked the exact dissipation identity (3). It yields integrability of the squared delayed intermediate predator and, together with bounded derivatives, critical extinction.
3. Checked the strict subcritical delayed exponential comparison and subsequent top-predator comparison for each finite nonnegative delay.
4. Verified that \(r>b+\alpha/m\) produces an eventual positive prey lower bound, then prey convergence to \(X=(r-b)/a\).
5. Checked the asymptotic proof beyond a formal expansion: \(y(t-\tau_1)\le e^{D\tau_1}y(t)\); slow variation of \(P\); polynomial lower bound for \(P\); compactness of normalized translated trajectories; the bounded-entire linear-delay Liouville argument; and the positive coefficient in \((1/P)'\).
6. Ran `python CHECK.py` against its embedded file to verify the exact algebraic identity, formal quadratic delay coefficient, and rational sharpness example. The program returned `CHECK_OK exact energy identity, quadratic coefficient, and sharpness example`.
7. As an additional finite diagnostic only, explicit Euler with step \(0.02\), constant histories \((x,y,z)=(3,0.5,0.2)\), parameters \((r,b,a,\alpha,k,m,d,\beta,\theta,v,p,q,\eta,e)=(4,1,1,0.5,0.3,1,2,2,0.5,1,1,1,1,1)\), and delays \((\tau_1,\tau_2)=(1.3,0.7)\), produced \(t y(t)\approx5.33747\) at \(t=2000\), approaching the proved value \(5.4\). This computation is not an infinite-time proof and no error bound is claimed for Euler.

The proof uses only ordinary scalar comparison, continuous dependence and boundedness for retarded equations, Barbalat's lemma, compactness, and a Fourier-support argument for the scalar linear limit. The asymptotic conclusion assumes finite fixed delays and a positive prey growth margin; it makes no assertion about stochastic systems or other delay types. Independent audit has not been performed.
