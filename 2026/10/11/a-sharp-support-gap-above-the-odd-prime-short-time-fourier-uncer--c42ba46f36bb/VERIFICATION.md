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

The proof is exact and self-contained modulo the classical Cauchy--Davenport inequality and the prime cyclic Fourier uncertainty inequality. Both cited inputs are used in Proposition 4.3 of the 2008 time-frequency paper, whose complete argument was read and independently reconstructed.

For any nonzero time rows, their Fourier support sizes obey
\[
\left|\operatorname{supp}\widehat h_j\right|\ge p+1-|\operatorname{supp}h_j|.
\]
Since there are at least \(\min(p,a+b-1)\) such rows and their input support sizes sum to \(ab\), this yields
\[
s\ge(p+1)\min(p,a+b-1)-ab.
\]
For \(a+b>p\), all cases except \(a=b=p\) give \(s\ge2p\). For \(a+b\le p\), all cases except \(a=b=1\) give \(s\ge2p\). The singleton exception gives \(s=p\).

For full-support inputs, if two Fourier rows are supported on characters, their ratio cocycle forces all time rows to have one frequency. In the case of a unique one-frequency row, a two-frequency adjacent ratio produces a three-frequency next row:
\[
\bigl(A\omega^{un}+B\omega^{vn}\bigr)
\bigl(A\omega^{u(n-1)}+B\omega^{v(n-1)}\bigr).
\]
The three frequency indices \(2u\), \(u+v\), and \(2v\) are distinct for odd prime \(p\) and \(u\ne v\). Its middle coefficient is
\[
AB(\omega^{-u}+\omega^{-v})\ne0.
\]
Therefore at least one non-character row has three frequencies, which raises the lower bound from \(2p-1\) to \(2p\). Every stated boundary is covered.

Sharpness is checked directly: \(V_{\delta_0}\delta_0\) has exactly one nonzero time row of length \(p\), and \(V_{\delta_0+\delta_1}\delta_0\) has exactly two such rows. With \(p=2\), \(f=(1,1/2)\), and \(g=(1,2)\), the time rows have Fourier support cardinalities one and two, showing exactly three support positions; thus the odd-prime hypothesis cannot be omitted.

A supplemental finite sanity run sampled Gaussian-integer signal/window pairs, checking \(19{,}891\) pairs at \(p=3\), \(19{,}999\) at \(p=5\), and \(20{,}000\) at \(p=7\) with exact zero tests. This sanity run is not an exhaustive search over complex pairs and is not used to establish the universal claim. There are no external infinite-proof certificates or numerical estimates used in the argument.
