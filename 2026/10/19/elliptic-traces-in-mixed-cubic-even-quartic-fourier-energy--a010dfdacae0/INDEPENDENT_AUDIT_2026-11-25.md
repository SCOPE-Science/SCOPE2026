# Independent mathematical audit

## correctness

PASS

Replayed frozen RESULT.md lines 55–104. The first-coordinate equation determines the ordered difference h; h=0 contributes q². In midpoint coordinates the cubic difference is −3hw²−h³/4 and the even-quartic difference is h(4v³+2cv)+vh³. For h≠0, counting w yields the baseline q(q−1) and the χ(3)-weighted character sum. For nonzero a,b, counting z²−h²=a/b by its two linear factors gives the full sum −χ(b), then removing h=0 subtracts χ(a); when a=0 or b=0 the direct constant-character counts give exactly the listed corrections, including a=b=0. The linear-argument character sum over v vanishes, and P_c(1/4)=(1+8c)/16, so the formula handles the common zero and distinct cubic roots without multiplicity. For c≠0 the cubic derivative has no common root, and the unique smooth point at infinity gives trace −C_c and Hasse. For c=0, (C,H,J)=(0,χ(−1),1); quadratic reciprocity on the prime field and the parity of extension degree give the claimed q mod 12 regimes. Nontrivial additive orthogonality in both coordinates gives the unnormalized mixed Fourier moment with q⁻². An independent direct convolution and separate formula evaluation for c=0, −1/8, α in F₅[α]/(α²−3) gave 1275, 1269, 1267 and in F₇[α]/(α²−6) gave 4851, 4837, 4739, with exact agreement. These are targeted checks besides the all-field proof. Frozen verify.py was inspected, not executed; verification_output.txt is recorded evidence only. The file's trace check computes the point count via the same character sum, rather than independently enumerating pairs (v,w); the trace identity is proved in the text.

## originality

PASS

No inspected source covers the mixed exact invariant. The strongest concrete comparisons compute either self-collisions, quadratic-surface extension, or a different ring/modulus. This decision credits only the mixed constant-input energy and its exact corrections, not extension estimates in general, the quadratic-character identity, or elliptic point counting.

## value

PASS

The mixed fourth moment is a natural invariant not determined by separate cubic and quartic energies. Its exact evaluation separates order-q branch effects from a bounded elliptic-trace fluctuation and resolves an exact three-regime law at the undeformed quartic, with uniform field and parameter coverage. This is useful as an exact Fourier/convolution benchmark, not a claimed sharp weighted extension bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
