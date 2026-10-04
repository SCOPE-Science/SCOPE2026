# Same-model review

## Correctness
PASS. The Gaussian calculation is exact: conditional null expectation gives e-value validity; alternative first and second moments give the stated e-power; the strictly decreasing forward-difference threshold proves all finite integer optimizer cases. The local and fixed-signal limits are direct consequences of that exact characterization. The packaged verifier independently checks the finite formulas on a deterministic grid and the asymptotic examples.

## Originality
PASS. The closest same-model literature optimizes different criteria. Dunn et al. optimize expected squared confidence-set radius; Tse and Davison compute finite-threshold rejection power; Strieder and Drton optimize asymptotic rejection power. Delong and Wüthrich (2025) is the closest conceptual source because it explicitly defines e-power and studies split sampling, but the inspected split-ratio analysis is numerical and concerns isotonic mean calibration rather than this scalar Gaussian theorem. The closest indexed prior result concerns null moment integrability of cross-fit and \(K\)-fold averages, not alternative expected-log growth.

Residual risk remains that broader e-value/Kelly-design literature may contain the same Gaussian optimizer under different notation, and the later 2025 calibration preprint is especially relevant. No inspected source stated the exact finite threshold rule, the \(|h|=1\) local phase, or the fixed-signal \(m_n=\sqrt n/|\mu|+O(1)\) law.

## Value
PASS. The split fraction is a central tuning choice for universal likelihood-ratio tests. The theorem gives an exact, self-contained design law for the e-power criterion and reveals that its optimum can be qualitatively different from published power- and confidence-radius optima. The sharp local boundary and fixed-signal vanishing-training-fraction law make the distinction operationally interpretable.

## Closest literature and limitations
The result is limited to the known-variance scalar Gaussian location model, a simple null, and a deterministic one-split e-value. E-power does not equal fixed-threshold rejection power, and no validity claim is made for choosing the split after seeing the same data. Relevant sources are arXiv:1912.11436, arXiv:2104.14676, DOI:10.1002/sta4.501, arXiv:2203.06748, and arXiv:2510.23821.

Same-model review: passed. Independent audit: not yet performed.
