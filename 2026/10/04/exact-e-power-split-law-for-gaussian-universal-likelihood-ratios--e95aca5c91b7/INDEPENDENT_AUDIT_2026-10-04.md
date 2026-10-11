# Independent mathematical audit

## correctness

PASS

Conditioning on the training mean \(\widehat\mu\), the evaluation log e-value is \((n-m)(\widehat\mu\bar Y_0-\widehat\mu^2/2)\). Under \(N(\mu,1)\), independence of the split gives \(\mathbb E\widehat\mu=\mu\), \(\mathbb E\widehat\mu^2=\mu^2+1/m\), hence the exact e-power formula. Direct subtraction gives the forward difference and therefore complete integer unimodality/tie characterization. The positivity threshold, local scaling, and fixed-signal expansion follow from that threshold relation. Independently, 3471 \((n,\mu)\) cases including every adjacent-tie value for \(2\le n<80\) were optimized over all integer splits and matched the threshold characterization exactly.

## originality

PASS

The Gaussian universal-inference literature analyzes size, rejection power, confidence-set geometry, and alternative split-ratio criteria. Strieder--Drton optimize asymptotic rejection power via noncentral split-chi-square approximations; Delong--Wüthrich study e-power for a different calibration problem and numerically vary a split ratio; Hao--Grünwald give general/exact Gaussian e-power results for other UI/RIPr constructions rather than a single fixed training/evaluation plug-in split. None of the inspected sources states or implies this scalar exact integer oracle law and its local/fixed-signal phase profile.

## value

PASS

E-power is a standard growth-rate criterion for e-values, and sample allocation is a central design choice in universal inference. The exact law reveals a qualitatively different optimum from fixed-fraction heuristics: under fixed signal the training fraction vanishes at rate \(n^{-1/2}\), while under local alternatives it has a nontrivial phase boundary at \(|h|=1\). That makes the calculation a motivated benchmark rather than a routine parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
