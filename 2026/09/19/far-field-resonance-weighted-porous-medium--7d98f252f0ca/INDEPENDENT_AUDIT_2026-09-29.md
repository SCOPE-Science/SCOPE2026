# Independent Audit — 2026-09-29

**Record:** `2026/09/19/far-field-resonance-weighted-porous-medium--7d98f252f0ca`  
**Disposition:** **PASSED**

## Correctness

**PASS** — The logarithmic-coordinate reduction and rate comparison check out. With r=σ/(p-1) and L=σ(m-1)+2(p-1), one has q=(m-1)r+2=L/(p-1), α+βr=1/(p-1), h=1/β=L/(m-p), and 1-βq=(2p-1-m)/(p-1). The source's far-field linearization supplies stable rates -q and -h, while d(log ξ)/dν=1 converts them exactly into ξ-powers. Variation of constants for βy_t+y=C_0e^{-qt}+lower order yields the forced, resonant, and free-mode cases, including K_log=C_0/β at q=h. Direct substitution also confirms that mr=N-2 makes the leading power's mth power radial harmonic and annihilates the forcing.

## Originality

**PASS** — The current Iagar–Munteanu preprint states the common leading tail and displays the two far-field stable rates, but the accessible text does not state the comparison surface m=2p-1, the universal second-order coefficient, the ξ^{-q}logξ resonance, or the harmonic cancellation surface as a second-order classification. Searches did not reveal this exact source-specific refinement. General critical-exponent logarithms and older diffusion-with-absorption asymptotics are prior art, and older homogeneous-absorption literature remains a residual originality risk.

## Scientific value

**PASS** — The result identifies which part of the next asymptotic term is universal and which retains profile memory, provides an eventual side of approach in the forced regime, and isolates two distinct codimension-one mechanisms. This is useful information for comparison and matched-asymptotic arguments beyond the source's common leading tail.

## Evidence checked

- Iagar and Munteanu, A porous medium equation with dominating weighted absorption: three types of self-similar solutions: https://arxiv.org/abs/2609.20397 — Current public preprint used to check the leading tail and far-field stable rates.
- Iagar and Munteanu, A porous medium equation with spatially inhomogeneous absorption. Part I: https://doi.org/10.1016/j.jmaa.2024.128965 — Prior related weighted-absorption work; no equivalent second-order trichotomy located in current search evidence.

Repository evidence was read at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6` / source-check commit `253a0fe5d0217455660a277f9adb940030e567ad`. A later repository-head comparison through `eff2c6312cec5b0dee5115e5f42211a853092dfb` found no changes under this record path, so the assigned source-tree SHA `83dcc64102c759d4575a13b952466dc263d18c44` is the tree audited. GitHub was used only as read-only evidence.

## Limitations

- This is a profile asymptotic theorem, not a large-time convergence result for arbitrary PDE solutions.
- The free-mode coefficient B_f is not determined from origin data, and higher-order terms when B_f=0 are not classified.
- Older homogeneous-absorption literature remains a residual originality risk; no inaccessible paper is claimed as read.

## Audit conclusion

This independent audit is scientifically complete on correctness, originality, and value. The record may remain at its source path without substantive research-file edits.
