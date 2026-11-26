# Independent mathematical audit

## correctness

PASS

Table 3 and the equations below it in Jang and Yen match the frozen six jump rates. Independently, for 1≤x<K one may keep y,z fixed and take exactly K−x consecutive tumor-birth jumps: the birth rate is positive and each total rate q is finite and positive along this route. For N=K−x>0, at each step the probability of the prescribed jump within T/N is (birth rate/q)(1−exp(−qT/N))>0. Their finite product guarantees the stated strict event before T and before x=0; x=K at time zero is immediate, including K=1. The frozen immune-death-then-birth path is valid too, since immune death is positive at y>0 and y=0 disables immune-mediated tumor death and immune regeneration. The argument requires no assumption about the fate of paths outside the finite chosen route. The paper's frozen branching threshold governs eventual branching extinction, not finite first passage; even the frozen linear chain with positive birth rate can hit a finite target below criticality. The 95% one-sided zero-count endpoint 0.000299528359776612… independently replays with /workspace/audit_evidence/replay.py (tumor); it bounds the sampled fixed-horizon law given independent identically distributed runs, not the exact CTMC via the tau-leaping data. The original package describes a bundled replay but the bound evidence includes no executable for this record; the proof and independent endpoint calculation do not rely on that script.

## originality

PASS

The supported contribution is a source-specific correction: the model as printed permits the very finite-horizon first passage declared impossible in its numerical interpretation. Finite positive-rate paths, extinction thresholds for linear branching, and zero-success confidence endpoints are standard ingredients, not independently original results. No earlier equivalent correction of this CTMC surfaced in the material checked.

## value

PASS

The source explicitly interprets a suppressive trajectory as ruling out a finite-threshold event in the coupled CTMC. The review confirms a substantive distinction between impossible and unobserved, and between the actual first-passage event and eventual extinction of a different process. That matters when using the model to interpret threshold crossings or zero Monte Carlo counts. This is a narrow exact correction, not a quantitative claim about practical risk or a rejection of strong immune suppression in the model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
