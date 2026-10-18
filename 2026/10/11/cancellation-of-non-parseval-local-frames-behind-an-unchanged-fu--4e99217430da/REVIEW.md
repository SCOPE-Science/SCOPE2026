# Independent mathematical audit

## correctness

PASS

At actual RESULT.md blob 1fae2c..., the scalar H=C example has V_1=V_2=H and weights 1, local singleton vectors 1/√2 and √(3/2). Thus S_1=½I, S_2=3/2 I, global S_{vφ}=2I=S_V, while C_Vz=(z,z), M=diag(½,−½), M C_Vz=(z/2,−z/2)≠0. Its compression on span(1,1) is zero because that vector maps into span(1,−1). Polarization gives exactly C_V* M C_V=0 iff P_RM|_R=0. Self-adjointness alone does not force M|_R=0. For repeated whole H=C^d, the necessary/sufficient constraint Σv_i²(S_i−I)=0 and positive definiteness are exact; solve one matrix from the others, giving real dimension (m−1)d² and a realizable open convex region by taking frames S_i^{1/2}e_j. These are exact operator calculations, not verifier claims.

## originality

PASS

The targeted primary Springer article actually prints the problematic implication after invoking only self-adjointness of a block-diagonal operator, and supplies the frame-operator identity but not its compression-level repair. Related frame literature treats direct sums and uniform local bounds; separate contemporaneous counterexamples to other controlled-fusion assertions do not address this specific Corollary 4.12(1). Thus this is a source-specific demonstrable correction, with finite-dimensional moduli quantifying the missing cancellation freedom.

## value

PASS

Correcting a false theorem about distributed fusion-frame processing protects inference from aggregate global frame operators to local Parsevalness, where redundant systems are a principal use case. A minimal exact counterexample, correct compression criterion and full repeated-block classification provide a reusable structural insight, not merely a cheap zero-check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
