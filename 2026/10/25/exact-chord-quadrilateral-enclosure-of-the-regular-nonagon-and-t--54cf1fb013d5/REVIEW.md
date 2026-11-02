# Independent mathematical audit

## correctness

PASS

The unit-circumradius regular nonagon admits 18 directed chord-normal directions j*pi/9, with support heights h_j=1 for even j and c=cos(pi/9) for odd j. Four support normals bound a polygon iff all cyclic gaps are in {1,...,8}. The exact support polygon shoelace formula reduces the global continuous area minimum to 1548 bounded quartets among choose(18,4)=3060. The bundled checker uses rational interval arithmetic in x=2cos(pi/9), the unique root x³-3x-1 in the bracket [18793852415/10¹⁰,18793852417/10¹⁰], with exact cosine/sine recurrences and positive denominators. Its 1548-case certificate yields exactly nine rotations of {0,5,9,13} as all chord winners, and separately 90 bounded four-odd-index edge-only cases yield exactly nine rotations of {1,5,9,13}; both losing families have strict rational separation. Independent full high-precision 1548-case enumeration agreed with winner count, area q_ch=2[c-(1+c²)cos(5pi/9)/2]/sin(5pi/9)+2c²tan(2pi/9), ratio 1.286857637640353..., edge-only optimum c²[3tan(2pi/9)+tan(3pi/9)] and strict gap about 0.02997756117. One optimal direction is genuinely a diagonal; affine maps preserve areas ratios/directions. All finite enumeration is exhaustive only after the proof reduces the continuum to 18 normals.

## originality

PASS

Vígh 2026 introduces chord quadrilateral enclosure, reports numeric experiments for some polygons but does not derive this regular nonagon exact formula, nine minimizers or strict edge-only penalty. The heptagon exact computation is a different n and edge-only optimum, and regular n enclosing parallelogram formulas solve a restricted family. The nonagon diagonal direction, exact all-config classification and strict arithmetic gap therefore remain best-of-knowledge new. An unindexed historical polygon optimization table is residual risk.

## value

PASS

The nonagon illustrates a structural phenomenon absent from the heptagon benchmark: allowing directions along polygon diagonals strictly improves the enclosing four-gon area versus restricting to original edges. Exact sharp values and all nine optimizer configurations give a natural rigorous test instance for a current chord-quadrilateral conjecture, even without resolving its general form. This is mathematically motivated rather than an arbitrary finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
