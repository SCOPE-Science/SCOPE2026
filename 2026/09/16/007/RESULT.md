# No universal fixed-patch cut-and-glue filter for homogeneous D=2 PEPS

## Context

Consider homogeneous PEPS on a square torus with local dimension 2 and bond dimension at most 2. The proposed cut-and-glue route asks for a fixed finite patch and a single fixed nonzero linear operator C on that patch, independent of the PEPS tensor A and of system size, that succeeds on every state and makes the filtered state product across the patch/complement cut (equivalently, the filtered patch marginal is pure).

## Result

No such universal fixed-patch operator exists. For every patch with m>=1 sites and every fixed nonzero linear C on its physical Hilbert space, some homogeneous D<=2 PEPS fails the demand: either C annihilates a homogeneous product state, or C leaves a homogeneous two-branch cat state entangled across the patch/complement cut.

## Proof

Homogeneous D=1 PEPS include every |v>^{tensor n}. Therefore universal nonzero postselection would require

C|v>^{tensor m} != 0

for every nonzero v in C^2.

Homogeneous D=2 PEPS also include, on every connected torus, the cat family

|v_1>^{tensor n}+|v_2>^{tensor n},

using a virtual all-0/all-1 tensor. For linearly independent v_1,v_2 and n-m>=1, the two complement vectors |v_1>^{tensor(n-m)} and |v_2>^{tensor(n-m)} are linearly independent. Hence the filtered cat is product across the cut if and only if C|v_1>^{tensor m} and C|v_2>^{tensor m} are collinear.

If the filter works for every such cat, all vectors C|v>^{tensor m} are pairwise collinear. Pure powers span Sym^m(C^2), so rank(C restricted to Sym^m(C^2)) <= 1. Rank zero annihilates every homogeneous product state. In rank one, write the restriction as |w><u|. Then

f(v)=<u|v>^{tensor m}

is a nonzero homogeneous binary form of positive degree. Over C it has a projective root v_* != 0, so C|v_*>^{tensor m}=0, again contradicting universal nonzero success.

This already defeats the first universal-filter step; no assumption about how the complement would subsequently be represented is needed.

## Numerical sanity check

`artifacts/verify_impossibility.py` contracts an explicit D=2 cat tensor on a 2x3 torus and samples the rank>=2, rank-one, and symmetric-subspace-killing branches. These computations illustrate the proof but are not needed for it.

## Limitations

The theorem concerns a single exact A-independent and n-independent linear postselection operator on one fixed patch. It does not rule out tensor-dependent or size-dependent filters, approximate disentangling, adaptive/multi-Kraus procedures, or bond-dimension witnesses that avoid a universal local filter.

## Reproducibility

Run `python3 artifacts/verify_impossibility.py` (NumPy).

## References

- O. Buerschaper, *Twisted Injectivity in PEPS and the Classification of Quantum Phases*, arXiv:1307.7763 (PEPS background; not the no-go theorem above).
