# Independent mathematical audit

## correctness

PASS

For positive sigma,gamma, 0<beta_L<beta_H, and positive high/low block durations, H=exp(t_H G_high), L=exp(t_L G_low), G_b=[[-sigma,b],[sigma,-gamma]], are strictly positive 2x2 matrices. Across all 20 words with 3 H and 3 L, cyclic trace/class reduction yields HHHLLL (6 words), HHLHLL (12), HLHLHL (2). Cayley–Hamilton gives exact tr(H²LHL²)-tr(H³L³)=tr(H)tr(L)K and tr((HL)³)-tr(H²LHL²)=tr(HL)K, K=-det[H,L]. Because [H,L]=u_H u_L[G_bH,G_bL] and det[G_bH,G_bL]=-sigma²(beta_H-beta_L)², K>0. At common positive determinant, Perron root strictly grows with trace, proving strict ordering clustered<middle<alternating. For beta_L<gamma, as beta_H varies from beta_L upward each multiplier increases strictly from <1 to infinity, giving strict ordered unique thresholds. Independent symbolic Cayley–Hamilton tests and all 20 word classes checked; numeric example matched but infinite range rests on algebra and positivity.

## originality

PASS

The epidemic literature establishes periodic environment effects and Floquet multipliers, and matrix trace identities are classical. What is assessed is the exact complete ordering of all balanced six-block SEIR calendars with unequal level durations and the strict separation of invasion boundaries. Existing resonance and outbreak scheduling papers do not state this ordered discrete classification in inspected material. Potential general two-matrix product inequalities remain a plausible strong-coverage risk.

## value

PASS

Changing only the order of fixed seasonal contact intensities can change the invasion verdict. An exact universal total ordering of all 20 balanced six-block calendars and the three strict intervention thresholds answers a canonical control scheduling question. This is more than verifying 20 examples because strictness holds for all continuous SEIR parameters and durations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
