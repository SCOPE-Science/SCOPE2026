# Independent mathematical audit

## correctness

PASS

The printed Section 4.2 choices combine a continuous latent-stage hazard with a boundary transfer. For the displayed transport equation with latent hazard one on ages below rho, characteristics multiply the boundary incidence by exp(-rho). Linearization therefore gives the scalar delay equation with reproduction ratio S0 eta (1-gamma) exp(-rho)/q. At the printed parameters S0=10, eta=0.59, rho=3 and q=100/161, an independent exact-rational replay gives the no-quarantine ratio 0.47292736242633965, so the printed simulation is already subcritical. A deterministic fixed latent residence instead has no pre-boundary progression loss and gives base ratio 9.499, threshold gamma=0.8947257606063796, and ratio 2.37475 at gamma=0.75. The delay characteristic-root argument in RESULT.md correctly proves these are exact linear thresholds rather than finite-time simulation observations.

## originality

PASS

The motivating article publicly states that its delay/quarantine simulations validate the model and that containment occurs at 75 percent quarantine, while the submitted calculation shows that the equations as printed contain an extra survival attenuation that makes even zero quarantine subcritical. The fixed-latency literature supplies the correct boundary-transfer construction but not this source-specific diagnosis or corrected 89.47 percent threshold. Targeted Resultary and web correction searches returned no prior correction of the Alanazi equations.

## value

PASS

The discrepancy reverses the qualitative disease-control regime at the published parameter set: the printed numerical equations are subcritical before quarantine, whereas a genuine fixed-delay model still requires nearly 89.5 percent quarantine. That directly affects interpretation of the paper's validation figures and containment claim, so it is a substantive model-consistency result rather than a cosmetic notation check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
