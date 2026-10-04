from decimal import Decimal

# Exact trace identities from the stated vector fields.
a = Decimal(40)
b = Decimal(2)
c = Decimal(22)
base_div = c - a - b
assert base_div == Decimal(-20)

reported = {
    'uncontrolled_e_0_5': [Decimal('16.9402'), Decimal('-3.4133'), Decimal('0'), Decimal('6.9890')],
    'uncontrolled_e_1': [Decimal('18.2980'), Decimal('-4.0706'), Decimal('0'), Decimal('8.0878')],
    'uncontrolled_e_3': [Decimal('19.5457'), Decimal('-4.1972'), Decimal('0'), Decimal('8.9684')],
    'controlled_r_minus_25': [Decimal('-3.2103'), Decimal('-13.5230'), Decimal('-23.3526'), Decimal('-22.5437')],
    'controlled_r_minus_30': [Decimal('-8.3379'), Decimal('-16.6337'), Decimal('-29.2114'), Decimal('-27.8364')],
}
expected = {
    'uncontrolled_e_0_5': base_div,
    'uncontrolled_e_1': base_div,
    'uncontrolled_e_3': base_div,
    'controlled_r_minus_25': base_div + Decimal(4) * Decimal(-25),
    'controlled_r_minus_30': base_div + Decimal(4) * Decimal(-30),
}

for key, vals in reported.items():
    s = sum(vals, Decimal(0))
    gap = s - expected[key]
    print(f'{key}: reported_sum={s} expected_sum={expected[key]} gap={gap}')
    assert s != expected[key]

assert expected['controlled_r_minus_25'] == Decimal(-120)
assert expected['controlled_r_minus_30'] == Decimal(-140)
print('VERIFY_OK')
