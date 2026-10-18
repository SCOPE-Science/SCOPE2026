# Independent mathematical audit

## correctness

PASS

Diagonal phase covariance of zero-temperature amplitude damping reduces arbitrary U to a real rotation with s²=t=|<1|U|0>|². Four composed Kraus matrices give the normalized 4x4 Choi partial-transpose determinant 16 det J^Gamma=a²[(1-a)²(1-b)²t⁴-b²]. For two qubits the partial transpose of a positive Choi state has at most one strictly negative eigenvalue, by product-vector intersection of every 2D complex subspace. Thus determinant sign determines PPT away from zero; boundary PPT follows by lowering b to a strictly PPT region and continuity. Peres–Horodecki gives entanglement breaking iff PPT. Hence threshold (1-a)(1-b)t²>=b. Optimizing t<=1 gives b<=(1-a)/(2-a), equal a=b gives q<=(3-√5)/2. An independent 250-case random unitary-parameter numeric Choi eigenvalue/determinant comparison corroborated all threshold regions; source verify.py was inspected but not blindly executed. The determinant identity, not finite samples, is the proof.

## originality

PASS

Generalized amplitude-damping Choi PPT/EB condition and absence of EB under directly cascaded positive-survival pure amplitude-damping steps are in Lami–Giovannetti; the population-interchanging endpoint can be recovered from that criterion and is not claimed wholly new. Cuevas et al already study interposed rotations and selected EB/repair phenomena. The accepted remainder classifies EVERY interposed U at unequal ordered a,b, including exact sharp threshold and order asymmetry; no such universal two-unequal-stage statement was located in inspected relevant original passages.

## value

PASS

Complete necessary-and-sufficient control classification for two ordered physical noise stages is a natural question: which, if any, coherent interstage rotations force entanglement breaking? The threshold and order asymmetry give a usable exact channel-theoretic boundary beyond a selected numerical example or mere EB existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
